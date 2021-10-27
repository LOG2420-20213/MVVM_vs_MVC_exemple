#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge-Station charging page. This page is used when a car is currently charging.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = ['PyQt5 UI code generator 5.15.0']
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Ui_Form(object):
    def __init__(self, widget, stationManager):
        self.widget = widget
        self.stationManager = stationManager
        self.setupUi(self.widget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 895)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1111, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 1111, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 160, 1111, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.battery_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.battery_value.setFont(font)
        self.battery_value.setText("")
        self.battery_value.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_value.setObjectName("battery_value")
        self.horizontalLayout_2.addWidget(self.battery_value)
        self.time_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.time_value.setFont(font)
        self.time_value.setText("")
        self.time_value.setAlignment(QtCore.Qt.AlignCenter)
        self.time_value.setObjectName("time_value")
        self.horizontalLayout_2.addWidget(self.time_value)
        self.pricing_value = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pricing_value.setFont(font)
        self.pricing_value.setText("")
        self.pricing_value.setAlignment(QtCore.Qt.AlignCenter)
        self.pricing_value.setObjectName("pricing_value")
        self.horizontalLayout_2.addWidget(self.pricing_value)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(470, 330, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.add_action_events()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Station is Charging!"))
        self.label_2.setText(_translate("Form", "Battery Level Estimation"))
        self.label_3.setText(_translate("Form", "Time Remaining Estimation"))
        self.label_4.setText(_translate("Form", "Pricing Estimation"))
        self.pushButton.setText(_translate("Form", "Stop Charging"))

    def add_action_events(self):
        self.pushButton.clicked.connect(self.on_click_stop_charging)

    def on_click_stop_charging(self):
        self.stationManager.stop_charging()

