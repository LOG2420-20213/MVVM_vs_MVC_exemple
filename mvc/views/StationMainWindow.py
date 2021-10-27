#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge-Station Main window. This window contains the pages add shows it.
"""

from PyQt5.QtWidgets import *

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = ['PyQt5 UI code generator 5.15.0']
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class Window(QWidget):

    def __init__(self, stationManager, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.stationManager = stationManager
        self.title = 'PolyCharge-Station'
        self.left = 250
        self.top = 100
        self.width = 1100
        self.height = 805
        self.setFixedSize(self.width, self.height)
        self.isClosing = True

    def closeEvent(self, a0):
        if self.isClosing:
            self.stationManager.exit_app()





