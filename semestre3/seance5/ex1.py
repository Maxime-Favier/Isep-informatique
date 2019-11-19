from numpy import matrix, inf, cos, sin, linspace, zeros
from numpy.linalg import norm
from math import sqrt

# 1. Normes de vecteurs
x = matrix([[1.], [2.], [3.]])
print("x=", x)
print("||x||_2=", norm(x, 2))
print("Check=", sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2))
print("||x||_INF=", norm(x, inf))
print("Check=", max(abs(x)))
print("||x||_1=", norm(x, 1))
print("Check=", sum(abs(x)))


# 2. Produit scalaire
def myDotProduct(x, y):
    n = x.shape[0]
    p = 0.0
    for i in range(n):
        p += x[i] * y[i]
    return p


x = matrix([[1.], [2.], [3.]])
y = matrix([[4.], [5.], [6.]])
print("x=", x)
print("y=", y)
print("<x,y>=", x.T * y)
print("Check=", myDotProduct(x, y))
