#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge abstract visitor class. (Visitor Pattern)
"""

from abc import ABCMeta

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class AbsVisitor(metaclass=ABCMeta):

    def processStation(self, station):
        pass
