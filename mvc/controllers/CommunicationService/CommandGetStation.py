#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concreate command class. This command class is used to get a station's information in the DB with the station id
"""
from Command import Command
import requests

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class CommandGetStation(Command):
    def __init__(self, id):
        self.id = id

    def execute(self):
        return {"state": "Available", "type": "ultra-fast", "battery_level": 25}
