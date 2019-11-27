from math import pi
from scipy import special
from quadtx import quadtx, quadgui
from floats import computeDigits
from numpy import nextafter, linspace, sqrt, sin
from pylab import plot, xlabel, ylabel, title, show


def myfunA(x):
    y = 1 / (3 * x - 1)
    return y


x = linspace(0., 2. / 3, 101)
y = myfunA(x)
plot(x, y)
xlabel("X")
ylabel("Y")
title("1/(3x-1)")
show()

try:
    Q, fcount = quadtx(myfunA, 0., 2. / 3.)
except ZeroDivisionError:
    print("Division par zéro")


def myfunB(x):
    return 1 / sqrt(1 + x ** 4)


x = linspace(0., 1, 100)
y = myfunB(x)
plot(x, y)
xlabel("X")
ylabel("Y")
title("1/sqrt(1+x**4)")
show()

Q, fcount = quadgui(myfunB, 0., 1.)
expected = 0.927037338650685959
print("exepected=", expected)
print("Q=", Q)
digits = computeDigits(expected, Q, 10)
print("digits=", digits)
print("fcount=", fcount)


def mysinc(x):
    return sin(x) / x


x = linspace(0., pi, 300)
y = mysinc(x)
plot(x, y)
xlabel("X")
ylabel("Y")
title("sin(x) / x")
show()

try:
    Q, fcount = quadtx(mysinc, 0., pi)
except RecursionError:
    print("Erreur de récursion")

afterzero = nextafter(0., pi)
print("afterzero", afterzero)
Q, fcount = quadtx(mysinc, afterzero, pi)
expected = 1.85193705198246617036
print("exepected=", expected)
print("Q=", Q)
digits = computeDigits(expected, Q, 10)
print("digits=", digits)
print("fcount=", fcount)


def mysincbis(x):
    if x == 0:
        y = 1
    else:
        y = sin(x) / x
    return y


Q, fcount = quadtx(mysincbis, 0., pi)
expected = 1.85193705198246617036
print("exepected=", expected)
print("Q=", Q)
digits = computeDigits(expected, Q, 10)
print("digits=", digits)
print("fcount=", fcount)


def betafun(t, z, w):
    y = t ** (z - 1.) * (1. - t) ** (w - 1.)
    return y


z = 8 / 3
w = 10 / 3
Q, fcount = quadtx(betafun, 0., 1, 1.e-6, z, w)
expected = 0.0348329096012058297782
print("exepected=", expected)
print("Q=", Q)
digits = computeDigits(expected, Q, 10)
print("digits=", digits)
print("special.beta", special.beta(z, w))
