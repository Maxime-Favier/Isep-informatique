from numpy import matrix
from numpy.linalg import solve
from lutx import backsubs, forward, argmax

A = matrix([[10., -7., 0.], [-3., 2., 6.], [5., -1., 5.]])
L = matrix([[1., 0., 0.], [0.5, 1., 0.], [-0.3, -0.04, 1.]])
U = matrix([[10., -7., 0.], [0, 2.5, 5.], [0., 0., 6.2]])
P = matrix([[1., 0., 0.], [0., 0., 1.], [0., 1., 0.]])
print("A=", A)
print("L=", L)
print("U=", U)
print("P=", P)
print("P*A=", P * A)
print("L*U", L * U)
# 2
U = matrix([[1., 2., 3., 4.], [0., 5., 6., 7.], [0., 0., 8., 9.], [0., 0., 0., 10.]])
print("U=", U)
e = matrix([[1.], [2.], [3.], [4.]])
b = U * e
print("exact=", solve(U, b))
print("b=", b)
print("x=", e)
print("backstubs(U,x)", backsubs(U, b))
# 3
L = matrix([[1., 0., 0., 0.], [2., 3., 0., 0.], [4., 5., 6., 0.], [7., 8., 9., 10.]])
print("L=", L)
e = matrix([[1.], [2.], [3.], [4.]])
b = L*e
print("exact", solve(L, b))
print("b=", b)
print("x=", e)
print('forward(L,b)=', forward(L, b))
# 4
A = matrix([[-3., 2., 6.], [5., -1., 5.], [10., -7., 0.]])
print("A=", A)
n = A.shape[0]
print("n=", n)

