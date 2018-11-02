# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendarpopupdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_calendarPopupDialog(object):
    def setupUi(self, calendarPopupDialog):
        calendarPopupDialog.setObjectName("calendarPopupDialog")
        calendarPopupDialog.resize(400, 342)
        self.verticalLayout = QtWidgets.QVBoxLayout(calendarPopupDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(calendarPopupDialog)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.frame = QtWidgets.QFrame(calendarPopupDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.firstDateEdit = QtWidgets.QDateEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstDateEdit.sizePolicy().hasHeightForWidth())
        self.firstDateEdit.setSizePolicy(sizePolicy)
        self.firstDateEdit.setObjectName("firstDateEdit")
        self.horizontalLayout_2.addWidget(self.firstDateEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(calendarPopupDialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.secondDateEdit = QtWidgets.QDateEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondDateEdit.sizePolicy().hasHeightForWidth())
        self.secondDateEdit.setSizePolicy(sizePolicy)
        self.secondDateEdit.setObjectName("secondDateEdit")
        self.horizontalLayout.addWidget(self.secondDateEdit)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(calendarPopupDialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okButton = QtWidgets.QPushButton(self.frame_3)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(calendarPopupDialog)
        QtCore.QMetaObject.connectSlotsByName(calendarPopupDialog)

    def retranslateUi(self, calendarPopupDialog):
        _translate = QtCore.QCoreApplication.translate
        calendarPopupDialog.setWindowTitle(_translate("calendarPopupDialog", "Dialog"))
        self.label.setText(_translate("calendarPopupDialog", "First date:"))
        self.label_2.setText(_translate("calendarPopupDialog", "Second date:"))
        self.okButton.setText(_translate("calendarPopupDialog", "Confirm first date"))

