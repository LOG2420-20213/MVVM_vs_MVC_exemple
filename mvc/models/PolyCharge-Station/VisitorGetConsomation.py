#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concrete visitor class. This class is used to get the charging consomation information (battery_level and charging time)
"""

from AbsVisitor import AbsVisitor

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class VisitorGetConsomation(AbsVisitor):

    def processStation(self, station):
        station.battery_level += station.percent_per_min
        battery_level_diff = int(station.state.target_percentage) - station.battery_level
        station.state.charging_time = min(battery_level_diff / station.percent_per_min, int(station.state.charging_time))


