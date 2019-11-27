from quadtx import quadtx, quadgui
from floats import computeDigits
from numpy import zeros
from pylab import plot, xlabel, ylabel, title, show, xscale, yscale


def humps(x):
    y = 1 / ((x - 0.3) ** 2 + 0.01) + 1 / ((x - 0.9) ** 2 + 0.04)
    return y


Q, fcount = quadgui(humps, 0, 1, 1.e-4)
exepected = 35.85832539549867
print("Q=", Q)
print("exepected", exepected)
digit = computeDigits(exepected, Q, 10)
print("digits=", digit)
print("fcount=", fcount)

err = zeros(13)
fcount = zeros(13)
for k in range(13):
    tol = 10**-k
    Q, fcount[k] = quadtx(humps, 0, 1, tol)
    err[k] = abs(Q - exepected)
    ratio = err[k]/tol
    print("%8.0e %7d %13.3e %9.3f" % \
          (tol, fcount[k], err[k], ratio))
plot(fcount, err, "bo")
title("Convergence of quadtx")
xlabel("Number of function calls")
ylabel("Error")
xscale("log")
yscale("log")
show()



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





from numpy import diff, array, arange
from interp import splineslopesNotAKnot

x = arange(1, 7)
print(x)
y = array([6., 8., 11., 7., 5., 2.])
T = sum(diff(x) * (y[0:-1] + y[1:]) / 2)
# T = h f(a)*f(b) /2
print("T=", T)
#D=sum(h**2*(d[1:]−d [0:−1])/12.)
#d = splineslopesNotAKnot(diff(x), )