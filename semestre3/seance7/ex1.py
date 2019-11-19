from numpy import vander, linspace, arange, array, vstack, zeros
from numpy.linalg import solve
from pylab import plot, title, show
from interp import polyinterp

x = array([-1., 0.,1.])
print("x=", x)
y = array([-1.,-1., 1.])
print("y=", y)
V = vander(x)
print("V=", V)
c = solve(V, y)
print("c=", c)
print("exact=", array([1, 0., -2., -5.]))

n = x.shape[0]
V = zeros((n, n))
for i in range(n):
    for j in range(n):
        V[i, j] = x[i] ** (n - j)
print("main V=", V)

nu = 100
x = arange(0, 4)
y = array([-5., -6., -1., 16.])
u = linspace(-0.25, 3.25, nu)
v = polyinterp(x, y, u)
plot(x, y, "o")
plot(u, v, "g-")
title("interpolation polynomiale de Lagrange")
show()