#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:02:18 2019

@author: ard
"""

x = [1,2,3];
y = 4;
z = 8;
if (y==7):
    x.append(y);
else:
    x.extend(str(z));

print(x);
