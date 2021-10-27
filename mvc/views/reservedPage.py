#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge-Station reserved page. This page is used when a station is reserved by a user.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = ['PyQt5 UI code generator 5.15.0']
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Ui_Form(object):
    def __init__(self, widget, stationManager, username):
        self.widget = widget
        self.username = username
        self.stationManager = stationManager
        self.setupUi(self.widget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1106, 901)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1101, 80))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 1101, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reverved_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.reverved_label.setFont(font)
        self.reverved_label.setAlignment(QtCore.Qt.AlignCenter)
        self.reverved_label.setObjectName("reverved_label")
        self.verticalLayout_2.addWidget(self.reverved_label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 121, 61))
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
        self.label.setText(_translate("Form", "PolyCharge-Station"))
        self.reverved_label.setText(_translate("Form", "This Station is reserved by user: {0}".format(self.username)))
        self.label_2.setText(_translate("Form", "Please enter your password"))
        self.pushButton.setText(_translate("Form", "Login"))

    def add_action_events(self):
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        is_valid_credentials = self.stationManager.login_username(self.username, self.lineEdit.text())

        if not is_valid_credentials:
            QMessageBox.question(self.widget, 'Message - PolyCharge-Station', "Error: Invalid Credentials", QMessageBox.Ok, QMessageBox.Ok)
            self.lineEdit.setText("")

