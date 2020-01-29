#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due January 31, 2020
Created on Tue Jan 28 15:27:46 2020
by Hannah Walcek
ThinkPython Exercise 7.1

This program creates the function mysqrt which accepts an integer, a, and uses
Newton's method to compute square roots. It also creates the function
test_square_root which compares mysqrt() to math.sqrt().
"""

#import math to use function sqrt
import math

def mysqrt(a):
    """
    Takes input, a, and computes the approximate squareroot.
    """
    #estimation for x
    x = a/2
    while True:
        #Newton's method
        y = (x + a/x) / 2
        #values may not be exactly equal, so threshold of 0.0000001 is made
        if abs(y-x) < 0.0000001:
            #if threshold is met, the value of x is returned
            return x
        #if value is not met, x is changed to the y value found
        else:
            x = y

def test_square_root():
    """
    Tests mysqrt() against math.sqrt() by calculating the difference and
    creates a table of a, mysqrt(a), math.sqrt(a), and diff.
    """
    a = 1
    #print the header
    print('a mysqrt(a)     math.sqrt(a)  diff')
    print('- ---------     ------------  ----')
    #while statement which prints squareroots for 1 through 10
    while a < 10:
        #prints values for table. note the formatting which ensures all
        #rows are lined up
        print(a, "%.11f" % mysqrt(a), "%.11f" % math.sqrt(a), 
              abs(mysqrt(a)-math.sqrt(a)))
        #adds 1 to a so the while statement repeats to the next number
        a = a+1
    
#runs test_square_root()
test_square_root()