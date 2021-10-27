#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge abstract state station class. (State Pattern)
"""

from abc import ABCMeta

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class AbsStateStation(metaclass=ABCMeta):
    def __init__(self):
        self.connector_type = None
        self.charging_time = None
        self.target_percentage = None
        self.username = None
