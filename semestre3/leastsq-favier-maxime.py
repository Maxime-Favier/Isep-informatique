from numpy import array, size, transpose, dot, linspace, vander
from numpy.linalg import solve, cond
from pylab import plot, title, show, xlabel, ylabel, legend
from leastsq import polyfitNormalEq, polyval
from math import log10

t = array([1900., 1910., 1920., 1930., 1940., 1950., 1960., 1970., 1980., 1990., 2000])
y = array([76., 92., 106., 123., 132., 151., 179., 203., 227., 250., 281.])
m = size(y)
print("number observation=", m)
n = 3
print("numb unknows", n)
print("polynomial degree", n - 1)
X = vander(t, n)
print("X=", X)
print("log10(cond(X))=", log10(cond(X)))
A = dot(transpose(X), X)
print("A=", A)
print("log10(cond(A))=", log10(cond(A)))
b = dot(transpose(X), y)
bet = solve(A, b)
print("bet=", bet)

x = linspace(1890, 2020, 100)
X = vander(x, n)
v = dot(X, bet)
plot(x, v)
plot(t, y, "o")
title("Polynomial least squares (Normal Equations)")
xlabel("Year")
ylabel("Millions")
show()

bet = polyfitNormalEq(t, y, 3)
u = linspace(1890, 2020, 100)
v = polyval(bet, u)
plot(u, v)
plot(t, y, "o")
xlabel("Year")
ylabel("Millions")
show()

bet = polyfitNormalEq(t, y, 3)
predict = polyval(bet, [2010.])
print("population en 2010 (prediction)", predict)
print("population reel 309,3 millions (2010)")

opt = ("-k", "--b", "-.g")
for polydeg in range(1, 4):
    # print(polydeg)
    bet = polyfitNormalEq(t, y, polydeg)
    u = linspace(1890, 2020, 100)
    v = polyval(bet, u)
    plot(u, v, opt[polydeg -1])
    xlabel("Year")
    ylabel("Millions")

title("Polynomial L.S. (Normal equations)")
plot(t, y, "o")
legend(('Degree 1', 'Degree 2', 'Degree 3'))
show()

for polydeg in range(1, 4):
    X = vander(t, polydeg)
    A = dot(transpose(X), X)
    print("deg", polydeg, ": log10(cond(A))=", log10(cond(A)), "Non ajusté")


# ex 2
from numpy import array, transpose, dot, linspace, vander, set_printoptions
from numpy.linalg import qr, solve, norm, cond
from pylab import plot, title, show, xlabel, ylabel
from leastsq import polyfit, polyval
from math import log10

t = array([1900., 1910., 1920., 1930., 1940., 1950., 1960., 1970., 1980., 1990., 2000])
y = array([76., 92., 106., 123., 132., 151., 179., 203., 227., 250., 281.])
n = 3
X = vander(t, n)
Q, R = qr(X)
print("log10(cond(R))=", log10(cond(R)))
z = dot(transpose(Q), y)
bet = solve(R, z)
print("beta=", bet)

bet = polyfit(t, y, n)
u = linspace(1890, 2020, 100)
v = polyval(bet, u)
plot(t, y, "o")
plot(u, v)
xlabel("Years")
ylabel("Millions")
show()

bet = polyfit(t, y, n)
v = polyval(bet, [2020.])
print("Prediction 2010", v)

