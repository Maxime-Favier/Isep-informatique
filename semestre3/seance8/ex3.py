from math import log2, ceil
from numpy import linspace, zeros
from fzerotx import bisection, bisectiongui
from pylab import plot, title, xlabel, ylabel, show, grid
from floats import computeDigits
from math import sqrt

e = 0.5e-3
i = ceil(log2(1 / e))
print("i=", i)


def myFunction(x):
    return x ** 2 - 2



x = linspace(0, 2, 100)
y = myFunction(x)
xs, history = bisectiongui(myFunction, 0, 2)
plot(x, y)
xlabel("x")
ylabel("f(x)")
title("f(x)=x^2-2")
grid()
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
title("convergence de Bisection")
grid()
show()
