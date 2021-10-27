#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concrete station state class. (State Pattern)
"""

from AbsStateStation import AbsStateStation

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Charging(AbsStateStation):
    def __init__(self, connector_type, charging_time, target_percentage, username):
        self.connector_type = connector_type
        self.charging_time = charging_time
        self.target_percentage = target_percentage
        self.username = username
