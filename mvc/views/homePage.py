#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge-Station home page. This page is used to start charging a car
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *

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
        Form.resize(1110, 894)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 1111, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 1111, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.connector_type = QtWidgets.QComboBox(Form)
        self.connector_type.setGeometry(QtCore.QRect(10, 160, 201, 20))
        self.connector_type.setObjectName("connector_type")
        self.connector_type.addItem("")
        self.connector_type.addItem("")
        self.connector_type.addItem("")
        self.connector_type.addItem("")
        self.connector_type.addItem("")
        self.charging_time = QtWidgets.QLineEdit(Form)
        self.charging_time.setGeometry(QtCore.QRect(375, 160, 201, 20))
        self.charging_time.setObjectName("charging_time")
        self.onlyInt = QIntValidator()
        self.charging_time.setValidator(self.onlyInt)
        self.target_percentage = QtWidgets.QLineEdit(Form)
        self.target_percentage.setGeometry(QtCore.QRect(760, 160, 201, 20))
        self.target_percentage.setObjectName("target_percentage")
        self.target_percentage.setValidator(self.onlyInt)
        self.charging_button = QtWidgets.QPushButton(Form)
        self.charging_button.setGeometry(QtCore.QRect(460, 220, 131, 51))
        self.charging_button.setObjectName("charging_button")
        self.logout_button = QtWidgets.QPushButton(Form)
        self.logout_button.setGeometry(QtCore.QRect(960, 0, 151, 23))
        self.logout_button.setObjectName("logout_button")

        self.retranslateUi(Form)
        self.add_action_events()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Select Charging Parameters"))
        self.label_5.setText(_translate("Form", "Connector Type"))
        self.label_3.setText(_translate("Form", "Charging Time (min)"))
        self.label_2.setText(_translate("Form", "Target Charge percentage (%)"))
        self.connector_type.setItemText(0, _translate("Form", "Type 1"))
        self.connector_type.setItemText(1, _translate("Form", "Type 2"))
        self.connector_type.setItemText(2, _translate("Form", "Type 3"))
        self.connector_type.setItemText(3, _translate("Form", "Type 4"))
        self.connector_type.setItemText(4, _translate("Form", "Commando"))
        self.charging_button.setText(_translate("Form", "Start Charging"))
        self.logout_button.setText(_translate("Form", "Logout"))

    def add_action_events(self):
        self.charging_button.clicked.connect(self.on_click_charging)
        self.logout_button.clicked.connect(self.logout)

    def on_click_charging(self):
        if str(self.connector_type.currentText()) != "" and self.charging_time.text() != "" and self.target_percentage.text() != "":
            self.stationManager.start_charging(str(self.connector_type.currentText()), self.charging_time.text(), self.target_percentage.text())
        else:
            QMessageBox.question(self.widget, 'Message - PolyCharge-Station', "Error: Please select all charging parameters", QMessageBox.Ok, QMessageBox.Ok)

    def logout(self):
        self.stationManager.logout()

