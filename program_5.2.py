#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due January 31, 2020
Created on Fri Jan 24 15:18:04 2020
by Hannah Walcek
ThinkPython Exercise 5.2

This program creates the function check_fermat and input_fermat using Fermat's
Last Theorem.
"""

def check_fermat(a, b, c, n):
    """This function takes integers for a, b, c, and n to determine whether or 
    not Fermat's Last Theorem is correct.
    """
    #first we set n>0 and the Fermat theorem to the unlikely case that there
    #is a solution
    if n > 2 and (a**n + b**n) == (c**n):
        print("Holy smokes, Fermat was wrong!")
    #any value less than or equal to 2 or that does not solve the equation is
    #set here in the else part of the function
    else:
        print("No, that doesn't work.")
        
def input_fermat():
    """This function is a bit more user friendly. It prompts the user for
    values a, b, c, and n and uses check_fermat to determine the whether the 
    theorem works or not.
    """
    #int() ensures the string from input() becomes an integer
    a = int(input('Integer value for a:')) 
    b = int(input('Integer value for b:'))
    c = int(input('Integer value for c:'))
    n = int(input('Integer value for n:'))
    check_fermat(a, b, c, n)

#here we run input_fermat() for the user
input_fermat()
    
        
        

