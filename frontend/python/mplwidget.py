from PyQt5 import QtWidgets
#from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

# Ensure using PyQt5 backend
#matplotlib.use('QT5Agg')


# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        #self.fig = Figure()
        #self.ax = self.fig.add_subplot(111)

        # Make with pyplot so it can be cleared
        self.fig, self.ax = plt.subplots(1, figsize=(30, 20))

        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)


        # These get wiped after starting the plot, so kinda useless
        self.ax.xaxis_date()

        plt.ylabel("Speed [km/h]")
        plt.title("Kusti polkee")

        xfmt = mdates.DateFormatter("%M:%S")
        self.ax.xaxis.set_major_formatter(xfmt)

        #xfmt = mdates.DateFormatter("%M:%S")
        #self.ax.xaxis.set_major_formatter(xfmt)
        # self.fig.autofmt_xdate()


# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)