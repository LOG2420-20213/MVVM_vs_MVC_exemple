#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concreate command class. This command class is used to update a station information on the DB
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


class CommandUpdateStation(Command):
    def __init__(self, station):
        self.station = station

    def execute(self):
        pass
