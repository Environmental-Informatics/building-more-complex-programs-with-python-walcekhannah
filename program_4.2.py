#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Due January 31, 2020
Created on Fri Jan 24 14:00:46 2020
by Hannah Walcek
ThinkPython Exercise 4.2

This program creates the functions polyline, arc, petal, and flower and uses
these to draw a set of flowers using turtles.
"""

#import turtle and math to use for future definitions
import turtle
import math


def polyline(t, n, length, angle):
    """Function that takes a turtle (t), line segments (n), 
    length, and angle (in degrees) to create a polyline.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    
def arc(t, r, angle):
    """Function that creates an arc with a turtle (t), with a radius (r), 
    and at an angle (in degrees). This uses the polyline function with inputs
    of step_length and step_angle.
    """
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    """Function that creates a petal with a turtle (t), radius (r),
    and at an angle (in degrees). This uses the arc function to place two arcs
    together.
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
        
def flower(t, p, r, angle):
    """Function that forms a flower with turtle (t), number of petals (p), 
    petal radius (r), and petal angle (in degrees). This uses the petal 
    function and repeats it p times.
    """
    for i in range(p):
        petal(t, r, angle)
        t.lt(360.0/p)

#here we name our turtle bob
bob = turtle.Turtle()

flower(bob, 10, 50, 70)
"""This center flower is created using bob. It has 10 petals which overlap, 
so the angle must be greater than 360/10. The number chosen is 70. 
It is also a bit small, so the radius given is 50.
"""

#here we move the turtle 150 units to the left
bob.penup()
bob.backward(150)
bob.pendown()

flower(bob, 7, 100, 360.0/7)
"""This left flower is created using bob. It has 7 petals which are evenly 
spaced, so the angle is 360.0/7. It is also larger than the center flower, 
so the radius given is 100.
"""

#here we move the turtle 300 units to the right
bob.penup()
bob.forward(300)
bob.pendown()

flower(bob, 20, 200, 360.0/20)
"""This right flower is created using bob. It has 20 petals which are evenly 
spaced, so the angle is 360.0/20. The radius given to it is 200 because the
angle is so small, the size needs to be offset with a large radius.
"""