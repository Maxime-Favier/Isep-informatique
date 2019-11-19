from numpy import matrix, ones
from numpy.linalg import solve, cond, norm
from scipy.linalg import hilbert
from math import log10
import sys
from lutx import lutx, forward, backsubs, luNoPivoting

# 1) 3)
A = matrix([[10., -7., 0.], [-3., 2., 6.], [5., -1., 5.]])
b = matrix([[7.], [4.], [6.]])
# 2)
print("conditionnement A", cond(A))
# 5)
L, U, p = lutx(A)
print("A=", A)
# 6)
c = b[p]
print("b=", b)
# 8)
y = forward(L, c)
print("y=",y)
# 10)
x = backsubs(U, y)
print("x=",x)
# 12)
A = matrix([[10., -7., 0.], [-3., 2., 6.], [5., -1., 5.]])
b = matrix([[7.], [4.], [6.]])
x = solve(A, b)
print("solve x=",x)