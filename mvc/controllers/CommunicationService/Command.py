#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge abstract command class. (Command Pattern)
"""

from abc import ABCMeta

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Command(metaclass=ABCMeta):

    @staticmethod
    def execute():
        pass
