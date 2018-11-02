using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Generic;
using OxyPlot;
using System.Collections.ObjectModel;

namespace IOT_Test
{

    public class ViewModelBase : System.ComponentModel.INotifyPropertyChanged
    {
        protected void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new System.ComponentModel.PropertyChangedEventArgs(propertyName));
        }
        public event System.ComponentModel.PropertyChangedEventHandler PropertyChanged;
    }

    public class MainViewModel : ViewModelBase
    {
        public MainViewModel()
        {
            this.Title = "Velocity";
            this.Points = new ObservableCollection<DataPoint>{};
        }

        public string Title { get; set; }


        private ObservableCollection<DataPoint> _Points;
        public ObservableCollection<DataPoint> Points
        {
            get { return this._Points; }
            set
            {
                if (this._Points != value)
                {
                    this._Points = value;
                    this.OnPropertyChanged("Points");
                }
            }
        }
    }
}
