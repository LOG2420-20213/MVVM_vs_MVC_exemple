#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge station manager. This class act as a middle man between the view and the logic.
"""

import argparse
from PyQt5.QtWidgets import *
import sys

sys.path.insert(1, r"..\views")
sys.path.insert(1, r"..\models\PolyCharge-Station")
sys.path.insert(1, r"..\models\StationService")
sys.path.insert(1, r".\CommunicationService")

from StationMainWindow import Window
import login
import homePage
import chargingPage
import reservedPage
import inErrorPage
import chargeCompletedPage
from StationUltraFast import StationUltraFast
from StationFast import StationFast
from StationStandard import StationStandard
from Communicator import Communicator
from CommandAuthentificationUsername import CommandAuthentificationUsername
from CommandAuthentificationCredit import CommandAuthentificationCredit
from CommandRegister import CommandRegister
from StationService import StationService
from CommandUpdateStation import CommandUpdateStation
from CommandGetStation import CommandGetStation
from VisitorUpdatePrice import VisitorUpdatePrice
from VisitorGetConsomation import VisitorGetConsomation
from Observer import Observer

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class StationManager(Observer):
    def __init__(self, id):
        station_db = Communicator.execute(CommandGetStation(id))
        if station_db["type"] == "ultra_fast":
            self.station = StationUltraFast(id, station_db)
        elif station_db["type"] == "fast":
            self.station = StationFast(id, station_db)
        else:
            self.station = StationStandard(id, station_db)

        self.view = Window(self)
        self.init_view()
        self.stationService = StationService(self.station, self.view, self)
        self.stationService.charge_completed.connect(self.station.chargeCompleted)
        self.station.attach(self)

    def init_view(self):
        if self.station.state.__class__.__name__ == "Available":
            self.view.widget = login.Ui_Form(QWidget(self.view), self)
            self.view.show()
        elif self.station.state.__class__.__name__ == "Reserved":
            self.view.widget = reservedPage.Ui_Form(QWidget(self.view), self, self.station.state.username)
            self.view.show()
        else:
            self.view.widget = inErrorPage.Ui_Form(QWidget(self.view), self)
            self.view.show()

    def update(self, station):
        if station.state.__class__.__name__ == "ChargeCompleted":
            self.view.widget.widget.deleteLater()
            self.view.isClosing = False
            self.view.close()
            self.view.isClosing = True
            self.view.widget = chargeCompletedPage.Ui_Form(QWidget(self.view), self)

            self.view.widget.battery_value.setText(str(station.battery_level))
            self.view.widget.time_value.setText(str(station.state.charging_time))
            self.view.widget.pricing_value.setText(str(station.price))
            self.view.show()

    def login_username(self, username, password):
        is_valid_credentials = Communicator.execute(CommandAuthentificationUsername(username, password))

        if is_valid_credentials:
            self.station.state.username = username
            self.view.widget.widget.deleteLater()
            self.view.isClosing = False
            self.view.close()
            self.view.isClosing = True
            self.view.widget = homePage.Ui_Form(QWidget(self.view), self)
            self.view.show()

        return is_valid_credentials

    def register(self, username, password):
        return Communicator.execute(CommandRegister(username, password))

    def login_credit(self, card_number, card_date, card_csv):
        is_valid_credentials = Communicator.execute(CommandAuthentificationCredit(card_number, card_date, card_csv))
        if is_valid_credentials:
            self.view.widget.widget.deleteLater()
            self.view.isClosing = False
            self.view.close()
            self.view.isClosing = True
            self.view.widget = homePage.Ui_Form(QWidget(self.view), self)
            self.view.show()

        return is_valid_credentials

    def start_charging(self, connector_type, charging_time, target_percentage):
        self.station.startCharge(connector_type, charging_time, target_percentage, self.station.state.username)
        Communicator.execute(CommandUpdateStation(self.station))

        self.view.widget.widget.deleteLater()
        self.view.isClosing = False
        self.view.close()
        self.view.isClosing = True
        self.view.widget = chargingPage.Ui_Form(QWidget(self.view), self)
        self.view.show()
        visitor = VisitorGetConsomation()
        self.station.accept(visitor)
        self.view.widget.battery_value.setText(str(self.station.battery_level))
        self.view.widget.time_value.setText(str(self.station.state.charging_time))
        visitor = VisitorUpdatePrice()
        self.station.accept(visitor)
        self.view.widget.pricing_value.setText(str(self.station.price))
        self.stationService.start()

    def stop_charging(self):
        self.stationService.stop()
        self.station.stopCharge()
        Communicator.execute(CommandUpdateStation(self.station))
        self.view.widget.widget.deleteLater()
        self.view.isClosing = False
        self.view.close()
        self.view.isClosing = True
        self.view.widget = homePage.Ui_Form(QWidget(self.view), self)
        self.view.show()

    def logout(self):
        self.station.state.username = None
        self.station.stopCharge()
        Communicator.execute(CommandUpdateStation(self.station))
        self.view.widget.widget.deleteLater()
        self.view.isClosing = False
        self.view.close()
        self.view.isClosing = True
        self.view.widget = login.Ui_Form(QWidget(self.view), self)
        self.view.show()

    def exit_app(self):
        if self.station.state.__class__.__name__ != "InError" and self.station.state.__class__.__name__ != "Reserved":
            self.station.state.username = None
            self.station.stopCharge()
            Communicator.execute(CommandUpdateStation(self.station))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fire PolyCharge-Station')
    parser.add_argument("-i", "--id", dest="id",  help='Station id', default=1, required=False)

    app = QApplication(sys.argv)
    stationManager = StationManager(parser.parse_args().id)
    sys.exit(app.exec_())
