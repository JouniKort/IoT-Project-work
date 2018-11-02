# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_w_hist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName("MplMainWindow")
        MplMainWindow.resize(881, 515)
        MplMainWindow.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.centralwidget = QtWidgets.QWidget(MplMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.UpperLayoutFrame = QtWidgets.QFrame(self.centralwidget)
        self.UpperLayoutFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UpperLayoutFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UpperLayoutFrame.setObjectName("UpperLayoutFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.UpperLayoutFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mplWidget = MplWidget(self.UpperLayoutFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplWidget.sizePolicy().hasHeightForWidth())
        self.mplWidget.setSizePolicy(sizePolicy)
        self.mplWidget.setStyleSheet("")
        self.mplWidget.setObjectName("mplWidget")
        self.horizontalLayout.addWidget(self.mplWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.rightSideMenuFrame = QtWidgets.QFrame(self.UpperLayoutFrame)
        self.rightSideMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightSideMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightSideMenuFrame.setObjectName("rightSideMenuFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rightSideMenuFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.startButton = QtWidgets.QPushButton(self.rightSideMenuFrame)
        self.startButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_2.addWidget(self.startButton, 0, QtCore.Qt.AlignTop)
        self.stopButton = QtWidgets.QPushButton(self.rightSideMenuFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setAutoDefault(False)
        self.stopButton.setDefault(False)
        self.stopButton.setFlat(False)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_2.addWidget(self.stopButton, 0, QtCore.Qt.AlignTop)
        self.historyButton = QtWidgets.QPushButton(self.rightSideMenuFrame)
        self.historyButton.setAutoDefault(False)
        self.historyButton.setDefault(False)
        self.historyButton.setFlat(False)
        self.historyButton.setObjectName("historyButton")
        self.verticalLayout_2.addWidget(self.historyButton, 0, QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.rightSideMenuFrame)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.UpperLayoutFrame)
        self.lowerLayoutHorizontal = QtWidgets.QHBoxLayout()
        self.lowerLayoutHorizontal.setObjectName("lowerLayoutHorizontal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.lowerLayoutHorizontal.addWidget(self.label)
        self.ipAddressLine = QtWidgets.QLineEdit(self.centralwidget)
        self.ipAddressLine.setObjectName("ipAddressLine")
        self.lowerLayoutHorizontal.addWidget(self.ipAddressLine)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.lowerLayoutHorizontal.addWidget(self.connectButton)
        self.verticalLayout.addLayout(self.lowerLayoutHorizontal)
        MplMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MplMainWindow)
        self.statusbar.setObjectName("statusbar")
        MplMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "IoT Speedometer"))
        self.startButton.setText(_translate("MplMainWindow", "Start"))
        self.stopButton.setText(_translate("MplMainWindow", "Stop"))
        self.historyButton.setText(_translate("MplMainWindow", "History"))
        self.label.setText(_translate("MplMainWindow", "IP:"))
        self.connectButton.setText(_translate("MplMainWindow", "Test connection"))

from mplwidget import MplWidget