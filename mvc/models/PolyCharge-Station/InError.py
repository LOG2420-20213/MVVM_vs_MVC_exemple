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


class InError(AbsStateStation):
    def __init__(self):
        super().__init__()
