#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge station service class. This service is used to update the charging information when a car is currently charging
"""

from PyQt5 import QtCore
import time
import sys

sys.path.insert(1, "..\PolyCharge-Station")

from VisitorGetConsomation import VisitorGetConsomation
from Communicator import Communicator
from CommandUpdateStation import CommandUpdateStation

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class StationService(QtCore.QThread):

    charge_completed = QtCore.pyqtSignal(object)

    def __init__(self, station, view, manager):
        QtCore.QThread.__init__(self)
        self.current_charging_time = 0
        self.station = station
        self.manager = manager
        self.view = view

    def run(self):
        self.start_charging_service()
        self.charge_completed.emit(str(self.current_charging_time))

    def start_charging_service(self):
        while self.station.battery_level < int(self.station.state.target_percentage) and int(self.station.state.charging_time) > 0:
            visitor = VisitorGetConsomation()
            self.station.accept(visitor)
            self.view.widget.battery_value.setText(str(self.station.battery_level))
            self.view.widget.time_value.setText(str(self.station.state.charging_time))
            Communicator.execute(CommandUpdateStation(self.station))
            self.station.state.charging_time -= 1
            self.current_charging_time += 1
            time.sleep(60)

        visitor = VisitorGetConsomation()
        self.station.accept(visitor)
        self.view.widget.battery_value.setText(str(self.station.battery_level))
        self.view.widget.time_value.setText(str(self.station.state.charging_time))

    def stop(self):
        self.terminate()

