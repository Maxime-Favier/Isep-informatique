from pylab import plot, xlabel, ylabel, title, show, text
from numpy import linspace
from math import pi
from optim import goldensectiongui
from floats import computeDigits

def cannsurface(r):
    V = 0.430
    return 2 * pi * (r ** 2) + 2*V / r


x = linspace(0.04, 2, 100)
y = cannsurface(x)
plot(x, y)
title("Soup Can problem")
xlabel("Radus")
ylabel("Surface")
xs, history = goldensectiongui(cannsurface, 0.04, 2)
show()
print("rayon optimal =", xs)
print("Sopt", cannsurface(xs))
xexact = (0.430 / (2 * pi)) ** (1 / 3)
print("digit corrects=", computeDigits(xexact, xs, 10))
print("cout unitaire", 0.002, "€")
print("surf opt", cannsurface(xexact))
print("prix opt", 0.002 * cannsurface(xexact), "€")