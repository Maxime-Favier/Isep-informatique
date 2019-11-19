from numpy import matrix
from numpy.linalg import solve, cond
from lutx import lutx, forward, backsubs
from math import log10

R = 1.0
vs = 10.0

A = matrix([[3 * R, -R, 0], [-R, 4 * R, -R], [0, -R, 4*R]])
print("A=", A)
print("cond(A)", cond(A))
print("perdus=", log10(cond(A)))
b = matrix([[vs], [0], [0]])
print("b=", b)
L, U, p = lutx(A)
c = b[p]
y = forward(L, c)
i = backsubs(U, y)
print("i=",i)