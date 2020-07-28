#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:33:51 2019

@author: ard
"""
x = [7,8,9];
y = 7;

for z in range (0,4):
    if y in x:
        print("this is before continue")
        continue
        print("this is after continue statement")
    print("this is continue");
