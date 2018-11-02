import sys
import urllib.request
from time import sleep

import dateutil
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtCore import pyqtSignal, QDateTime
from PyQt5.QtGui import QColor
from ui import Ui_MplMainWindow
from calendrpopupui import Ui_calendarPopupDialog
import json
import datetime
import random
import pandas
import requests
import schedule

from matplotlib import pyplot as plt
import matplotlib.dates as mdates

# Use "test" for generating fake data locally
#ip = "http://192.168.8.102:3001"
ip = "test"

# How often to plot in seconds, since it can be slow with larger datasets
plot_interval = 0.3

# How much sleep between retrieving new data
data_request_interval = 1

# Max size of the dataframe for plotting
dataframe_max_length = 100


class MainWindow(QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        self.setupUi(self)

        self.startButton.clicked.connect(self.start_button_pressed)
        self.stopButton.clicked.connect(self.stop_button_pressed)
        self.connectButton.clicked.connect(self.connect_button_pressed)
        self.historyButton.clicked.connect(self.history_button_pressed)
        self.ipAddressLine.setText(ip)

        self.w = None

        self.plotpoints = pandas.DataFrame({"Datetime": [], "Value": []})
        self.datathread = GetData()

        schedule.every(plot_interval).seconds.do(self.plot)

    def start_button_pressed(self):
        self.datathread.start()
        self.datathread.datasig.connect(self.receive_data)

    def stop_button_pressed(self):
        self.datathread.stop()

    def connect_button_pressed(self):
        # The lazy way
        global ip
        ip = self.ipAddressLine.text()

        print("IP:", ip)

    def history_button_pressed(self):
        date1 = None
        date2 = None

        print("Opening calendar dialog")
        self.w = CalendarWindow()

        if self.w.exec():
            #print(self.w.dates)
            date1 = self.w.dates[0]
            date2 = self.w.dates[1]

        # Convert QDate to datetime
        date1 = QDateTime(date1).toPyDateTime()
        date2 = QDateTime(date2).toPyDateTime()

        #date1 = date1.isoformat() # No ms or Z
        # Format to the way that backend wants it
        date1 = date1.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        date2 = date2.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        if ip == "test":
            # Clear dataframe
            self.plotpoints = self.plotpoints.iloc[0:0]

            for i in range(1000):
                data = self.datathread.data_processing()
                self.plotpoints.loc[data[0]] = data[1]
        else:
            data = self.get_data_history(date1, date2)
            #print(data)

            #plt.clf()
            # Clear dataframe
            self.plotpoints = self.plotpoints.iloc[0:0]
            for i in data:
                timestamp = i["timestamp"]
                time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
                value = i["value"]

                self.plotpoints.loc[time] = value

        self.plot()

    def get_data_history(self, timestamp1, timestamp2):
        data = None

        with urllib.request.urlopen(ip + "/api/data/" + timestamp1 + "/" + timestamp2) as url:
            response = url.getcode()
            print("Response:", response)

            if response == 200:
                data = json.loads(url.read().decode())
            else:
                print("Could not retrieve data")

            return data

    def receive_data(self, datasig):
        time = datasig[0]
        value = datasig[1]

        self.plotpoints.loc[time] = value
        #self.plotpoints.info()

        # If dataframe is too long start deleting old data
        if len(self.plotpoints.index) > dataframe_max_length:
            self.plotpoints = self.plotpoints.drop(self.plotpoints.index[0])

        schedule.run_pending()

    def plot(self):
        # Clear plot, because it doesn't do that automatically
        plt.cla()

        # Need to set this after clearing
        plt.ylabel("Speed [km/h]")
        plt.title("Kusti polkee")

        xfmt = mdates.DateFormatter("%M:%S")
        self.mplWidget.canvas.ax.xaxis.set_major_formatter(xfmt)

        self.mplWidget.canvas.ax.plot(self.plotpoints, "g-")
        self.mplWidget.canvas.draw()


class CalendarWindow(QDialog, Ui_calendarPopupDialog):
    def __init__(self, parent=None):
        super(CalendarWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.okButton.clicked.connect(self.ok_button_clicked)

        self.first_date = None
        self.second_date = None

        self.dates = ()

    def ok_button_clicked(self):
        selected_date = self.calendarWidget.selectedDate()
        #print("Selected date:", selected_date)

        if self.first_date is None:
            self.firstDateEdit.setDate(selected_date)
            self.first_date = selected_date
            self.okButton.setText("Confirm second date")

        elif self.first_date is not None and self.second_date is None:
            self.secondDateEdit.setDate(selected_date)
            self.second_date = selected_date
            self.okButton.setText("Confirm dates")

        elif self.first_date is not None and self.second_date is not None:
            self.dates = (self.first_date, self.second_date)
            self.done(1)


class GetData(QtCore.QThread):
    # Signal needs to be declared here
    datasig = pyqtSignal(tuple)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.data = ()
        self.running = False

        if ip != "test":
            # Turn sensor on
            send_commands(1)
            sleep(1)

    def run(self):
        self.running = True
        while self.running:
            self.data = self.data_processing()

            self.datasig.emit(self.data)
            sleep(data_request_interval)

    def stop(self):
        self.running = False

        if ip != "test":
            # Turn sensor off
            send_commands(0)

    def json_gen(self):
        data = {"value": random.random()*10, "timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
        data = json.dumps(data)

        return data

    def json_depack(self, data):
        data = json.loads(data)

        return data

    def get_data_latest(self):
        data = None

        with urllib.request.urlopen(ip + "/api/sensor/latest") as url:
            response = url.getcode()
            print("Response:", response)

            if response == 200:
                data = json.loads(url.read().decode())
            else:
                print("Could not retrieve data")

            return data


    def data_processing(self):
        if ip == "test":
            # Testing data
            data = self.json_gen()
            data = self.json_depack(data)
        else:
            # Real data
            data = self.get_data_latest()

        timestamp = data["timestamp"]
        time = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        value = data["value"]

        data = (time, value)

        return data


def send_commands(cmd):
    send = {}

    if cmd == 1:
        send = {"sensor": "on"}
    elif cmd == 0:
        send = {"sensor": "off"}
    else:
        print("Bad command")

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.put(ip + "/api/sensor", data=json.dumps(send), headers=headers)
    print("Response:", response)


def main():
    app = QApplication(sys.argv)
    w = MainWindow()

    p = w.palette()
    p.setColor(w.backgroundRole(), QColor.fromRgb(249,249,249))
    w.setPalette(p)

    plt.gcf().set_facecolor('#F9F9F9')

    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

