#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import matrix
from numpy.linalg import cond, solve
from math import log10
from lutx import (
    lutx, forward, backsubs
)

r1 = 100.
r2 = 50.
r3 = 50.
r4 = 100.
r5 = 200.
vs = 12.
A = matrix([[r1+r2, -r2, -0], [-r2, r3 + r4 + r2, -r4], [0., -r4, r5 + r4]])
print(A)
print("condi(A)", cond(A))
print("perdu", log10(cond(A)))
print("restants", log10(2 ** 53 / cond(A)))
b = matrix([[vs], [0], [0]])
print("b=", b)
L, U, p = lutx(A.copy())  # 1) Decompose
c = b[p]  # 2) Permute
y = forward(L, c)  # 3) Resout Ly=c
i = backsubs(U, y)  # 4) Resout Ui=y
print("i=", i)

iexact = solve(A, b)
print("i solve=", iexact)