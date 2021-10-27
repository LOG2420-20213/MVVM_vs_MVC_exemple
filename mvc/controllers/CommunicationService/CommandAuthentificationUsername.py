#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concreate command class. This command class is used to authenticate a user with his username and password.
"""
from Command import Command
import requests

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class CommandAuthentificationUsername(Command):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def execute(self):
        return True

