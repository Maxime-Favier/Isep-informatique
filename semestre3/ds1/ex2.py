from numpy import matrix
from numpy.linalg import solve

r1 = 100.
r2 = 50.
r3 = 50.
r4 = 100.
r5 = 200.
vs = 12.
A = matrix([[r1, 0., 0., r2, 0.], [0., r3, 0., -r2, r4], [0., 0., r5, 0., -r4], [1., -1., 0., -1., 0.],
            [0., 1., -1., 0., -1.]])
print("A=", A)
b = matrix([[vs], [0.], [0.], [0.], [0.]])
print("b=", b)

i = solve(A, b)
print("i=", i)