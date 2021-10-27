#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concrete station class. This class is a type of station. The type is standard
"""

from Station import Station

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class StationStandard(Station):

    def __init__(self, id, station_db):
        super().__init__(id, station_db)
        self.price_per_min = 2
        self.percent_per_min = 1
        self.state = super().init_state(station_db)
