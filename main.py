#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:32:02 2023

@author: nebiyousamuel
"""

# main.py
import financial_script

principal_amount = 1000
rate_of_interest = 5
time_period = 2

simple_interest = financial_script.calculate_simple_interest(principal_amount, rate_of_interest, time_period)
print("Simple Interest:", simple_interest)
