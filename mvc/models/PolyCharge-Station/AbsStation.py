#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge abstract station class.
"""

from abc import ABC, abstractmethod

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class AbsStation(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @abstractmethod
    def startCharge(self, connector_type, charging_time, target_percentage, username):
        pass

    @abstractmethod
    def stopCharge(self):
        pass

    @abstractmethod
    def chargeCompleted(self, charging_time):
        pass