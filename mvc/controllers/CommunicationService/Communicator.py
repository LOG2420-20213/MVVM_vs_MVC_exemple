#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge command executer. This class is used to execute commands.
"""

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Communicator:
    @classmethod
    def execute(cls, command):
        return command.execute()
