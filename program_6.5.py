#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due January 31, 2020
Created on Tue Jan 28 14:49:13 2020
by Hannah Walcek
ThinkPython Exercise 6.5

This program creates the function gcd which finds the greatest common divisor
between two values, a and b.
"""

def gcd(a,b):
    """
    This function takes two integers, a and b, and finds their greatest
    common divisor.
    """
    #when b is 0, the greatest common divisor is a
    if b == 0:
        return a
    #using the remainder (a%b) as the next input for b
    else:
        return gcd(b, a%b)

