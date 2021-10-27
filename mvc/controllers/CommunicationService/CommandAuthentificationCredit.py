#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PolyCharge concreate command class. This command class is used to authenticate a user with his credit card.
"""
from Command import Command

__author__ = 'Kevin Gauthier'
__copyright__ = 'Copyright 2020, PolyCharge'
__credits__ = []
__version__ = '0.1.0'
__maintainer__ = 'Nikolay Radoev'
__email__ = 'nikolay.radoev@polymtl.ca'
__status__ = 'Done'


class CommandAuthentificationCredit(Command):
    def __init__(self, credit_card_number, credit_card_date, credit_card_cvc):
        self.credit_card_number = credit_card_number
        self.credit_card_date = credit_card_date
        self.credit_card_cvc = credit_card_cvc

    def execute(self):
        return true

