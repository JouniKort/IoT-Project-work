using Newtonsoft.Json;
using OxyPlot.Wpf;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net;
using System.Windows;
using System.Windows.Controls.Primitives;
using System.Windows.Media;
using System.Windows.Threading;

using Microsoft.Maps.MapControl.WPF;

namespace IOT_Test
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    /// 

    public partial class MainWindow : Window
    {
        private MainViewModel mvm = new MainViewModel();
        private int interval = 1000;
        private string ip;
        DispatcherTimer timer = new DispatcherTimer();

        private MapPolyline LpC = Routes.Lappeenranta();
        private Location LatestLocation;
        private Pushpin Pointer = new Pushpin();

        public MainWindow()
        {
            InitializeComponent();
            string credentials = System.Configuration.ConfigurationManager.AppSettings["Bing"];
            ip = System.Configuration.ConfigurationManager.AppSettings["IP"];
            BingMap.CredentialsProvider = new ApplicationIdCredentialsProvider(credentials);
            
            plot.Axes.Add(new DateTimeAxis { Position = OxyPlot.Axes.AxisPosition.Bottom, StringFormat = "hh:mm:ss"});
            plot.Series[0].ItemsSource = mvm.Points;
            timer.Tick += (s, e) =>
            {
                GetData();
            };
            timer.Interval = new TimeSpan(0,0,0,0,interval);


            BingMap.Children.Add(LpC);
            LatestLocation = LpC.Locations[0];
        }

        private void GetData()
        {
            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            string json = string.Empty;
            string url = ip + @"/api/sensor/latest";

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;
            try
            {
                using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                using (Stream stream = response.GetResponseStream())
                using (StreamReader reader = new StreamReader(stream))
                {
                    json = reader.ReadToEnd();
                }

                Datapoint dp = JsonConvert.DeserializeObject<Datapoint>(json);
                if (dp == null)
                {
                    return;
                }
                DateTime d = DateTime.Parse(dp.Timestamp, null, System.Globalization.DateTimeStyles.RoundtripKind);
                mvm.Points.Add(new OxyPlot.DataPoint(OxyPlot.Axes.DateTimeAxis.ToDouble(d), dp.Value));
                Console.WriteLine(dp.Value + " " + dp.Timestamp);

                double km = dp.Value / 3.6 * interval / 1000 / 1000;

                LatestLocation = Utils.GetLocation(km, LatestLocation, LpC);

                BingMap.Center = LatestLocation;

                BingMap.Children.Remove(Pointer);

                Pointer.Location = new Location(LatestLocation);
                Pointer.Content = Utils.TotalDistance;
                Pointer.Background = new SolidColorBrush(Colors.Red);
                Pointer.Foreground = new SolidColorBrush(Colors.White);

                BingMap.Children.Add(Pointer);
            }
            catch (Exception e)
            {

            }
        }

        private void ToggleButton_Click(object sender, RoutedEventArgs e)
        {
            ToggleButton button = sender as ToggleButton;
            string url = ip + @"/api/sensor";

            var httpWebRequest = (HttpWebRequest)WebRequest.Create(url);
            httpWebRequest.ContentType = "application/json";
            httpWebRequest.Method = "PUT";

            string json = "";

            if (button.IsChecked == true)
            {
                json = JsonConvert.SerializeObject(new { sensor = "on" });
                timer.Start();
            }
            else
            {
                json = JsonConvert.SerializeObject(new { sensor = "off" });
                timer.Stop();
            }

            using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            {
                streamWriter.Write(json);
            }

            var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            mvm.Points.Clear();

            string time1 = t1.SelectedDate.Value.ToString("yyyy-MM-dd'T'HH:mm:ss.fffK", CultureInfo.InvariantCulture);
            string time2 = t2.SelectedDate.Value.ToString("yyyy-MM-dd'T'HH:mm:ss.fffK", CultureInfo.InvariantCulture);

            ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            string json = string.Empty;
            string url = ip + @"/api/data/"+time1+"/"+time2;

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;
            try
            {
                using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
                using (Stream stream = response.GetResponseStream())
                using (StreamReader reader = new StreamReader(stream))
                {
                    json = reader.ReadToEnd();
                }

                List<Datapoint> dps = JsonConvert.DeserializeObject<List<Datapoint>>(json);
                if (dps.Count == 0)
                {
                    return;
                }
                foreach(Datapoint dp in dps)
                {
                    DateTime d = DateTime.Parse(dp.Timestamp, null, System.Globalization.DateTimeStyles.RoundtripKind);
                    mvm.Points.Add(new OxyPlot.DataPoint(OxyPlot.Axes.DateTimeAxis.ToDouble(d), dp.Value));
                }
            }
            catch (Exception ex)
            {

            }
        }
    }

    public class Datapoint
    {
        public string Timestamp { get; set; }
        public double Value { get; set; }
        public string Id { get; set; }
    }
}
