from optim import goldensection, goldensectiongui
from pylab import plot, xlabel, ylabel, title, show, text
from numpy import linspace
from floats import computeDigits
from math import pi


def minushumps(x):
    return -1 / ((x - 0.3) ** 2 + 0.01) - 1 / ((x - 0.9) ** 2 + 0.04)


x = linspace(-1, 2, 100)
y = minushumps(x)
plot(x, y, "-")
title("-humps(x)")
xopt, fopt = goldensectiongui(minushumps, -1, 2)
print("xopt=", xopt)
print("fopt=", fopt)
show()

xoptexact = 0.30037562161975485562
digits = computeDigits(xoptexact, xopt, 10)
print("correct digits=", digits)

