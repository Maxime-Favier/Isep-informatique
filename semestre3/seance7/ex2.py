from floats import computeDigits, absoluteError
from numpy import logspace, zeros, log10
from pylab import plot, xlabel, ylabel, title, show, xscale, legend
from math import sin, cos


def myfonc(x):
    y = sin(x)
    return y


x, h = 1.0, 1.e-4
expected = cos(x)
g = (myfonc(x + h) - myfonc(x)) / h
d = computeDigits(expected, g, 10)
print("g=", g, "expect", d)
g= (myfonc(x + h) - myfonc(x-h)) / (2*h)
print("g=", g)