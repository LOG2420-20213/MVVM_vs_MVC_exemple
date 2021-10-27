#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concrete station class. This class is the main class of PolyCharge-Station. It represent the station.
"""

from Charging import Charging
from Available import Available
from Reserved import Reserved
from InError import InError
from ChargeCompleted import ChargeCompleted
from AbsStation import AbsStation
from Communicator import Communicator
from CommandUpdateStation import CommandUpdateStation
import random

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Station(AbsStation):
    def __init__(self, id, station_db):
        self.id = id
        self.state = self.init_state(station_db)
        self.battery_level = None
        self.price_per_min = None
        self.percent_per_min = None
        self.price = 0
        self.observers = []

    def __dict__(self):
        station_dict = self.state.__dict__
        station_dict["id"] = self.id
        station_dict["state"] = self.state.__class__.__name__
        station_dict["battery_level"] = self.battery_level

        return station_dict

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def init_state(self, station_db):
        if station_db["battery_level"]:
            self.battery_level = float(station_db["battery_level"])
        else:
            self.battery_level = None

        if station_db["state"] == "Available":
            return Available(None)
        elif station_db["state"] == "Reserved":
            return Reserved(station_db["username"])
        else:
            return InError()


    def accept(self, visitor):
        visitor.processStation(self)

    def startCharge(self, connector_type, charging_time, target_percentage, username):
        self.battery_level = random.randrange(0, 50)
        self.state = Charging(connector_type, charging_time, target_percentage, username)

    def stopCharge(self):
        self.battery_level = None
        self.price = 0
        self.state = Available(self.state.username)

    def chargeCompleted(self, charging_time):
        self.state = ChargeCompleted(charging_time, self.state.username)
        Communicator.execute(CommandUpdateStation(self))
        self.notify()
