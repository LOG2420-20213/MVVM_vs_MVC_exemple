#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concrete visitor class. This class is used to update the pricing information
"""

from AbsVisitor import AbsVisitor

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class VisitorUpdatePrice(AbsVisitor):

    def processStation(self, station):
        station.price = station.price_per_min * station.state.charging_time

