from fzerotx import secantgui
from floats import computeDigits
from math import sqrt

def myFonction(x):
    return x ** 2 - 2


xs, hystory = secantgui(myFonction, 1, 2)
print("xs=", xs)
xeact = sqrt(2)
print("correct digit=", computeDigits(xeact, xs, 10))
print("itérations", len(hystory))
