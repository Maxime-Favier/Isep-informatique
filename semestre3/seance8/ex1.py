from math import sqrt
from fzerotx import newton, newtongui
from pylab import plot, xlabel, ylabel, title, grid, show
from floats import computeDigits
from numpy import linspace, vectorize, exp, zeros


def myFunction(x):
    return x ** 2 - 2


def myFunctionPrime(x):
    return 2 * x


N = 100
x = linspace(1., 2., N)
y = myFunction(x)
plot(x, y)
xlabel("x")
ylabel("f(x)")
title("f(x)=x^2-2")
xs, history = newtongui(myFunction, 1, myFunctionPrime)
show()

print("xs=", xs)
xexact = sqrt(2)
d = computeDigits(xexact, xs, 10)
print("correct decimal digits=", d)
print("Itération=", len(history))

n = len(history)
digits = zeros(n)
for i in range(n):
    xs = history[i]
    digits[i] = computeDigits(xexact, xs, 10)

plot(range(n), digits, "ro")
xlabel("Itération")
ylabel("Number of digits")
title("convergence de Newtion")
grid()
show()
