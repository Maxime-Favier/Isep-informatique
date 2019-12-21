#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi
from numpy import array, linspace
from odes import ode23tx
from pylab import plot, show
from fzerotx import fzerotx

F = 10.e6
D = 0.8
d = 0.1
E = 200.e6
L = 1.5
a = 1.
b = L - a
I = (pi * (D ** 4 - d ** 4)) / 32
print("I=", I)


def deviation(u, x):
    if x < a:
        M = (F * b * x) / L
    else:
        M = (F * a * (L - x)) / L
    udot = array([u[1], M/(E*I)])
    return udot

u0 = [0, -0.13819651577772565]
xspan = [0, L]
xout, uout = ode23tx(deviation, xspan, u0)
print("uout", uout)
print(xout)
plot(xout, uout[:,0], "-o")
show()

xspan = [0, a]
print(uout[-1, 0])

def rightDeviation(dy0):
    u0 = [0, dy0]
    xspan = [0, L]
    xout, uout = ode23tx(deviation, xspan, u0)
    return uout[-1, 0]

c, h = fzerotx(rightDeviation, -1, 0)
print(c)