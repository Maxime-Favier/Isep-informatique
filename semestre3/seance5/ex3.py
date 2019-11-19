from numpy import matrix, zeros

# 1. Matrice additions
A = matrix([[1., 2.], [3., 4.], [0., 1.]])
B = matrix([[5., 6.], [7., 8.], [-1., 1.]])
print("A=", A)
print("B=", B)
print("A+B=", A + B)

# 2. Matrices transposee
print("A=", A)
print("A^T=", A.T)

# 3. Matrices multiplication par un scalaire
alpha = 2
print("A=", A)
print("A*alpha", A * alpha)

# 4. produit matrice vecteur
x = matrix([[1.], [2.]])
print("A=", A)
print("x=", x)
print("A*x=", A * x)

# 4. produit matrice-matrice
C = matrix([[1., 2., 3., 4.], [5., 6., 7., 8.]])
print("A=", A)
print("C=", C)
print("A*C", A*C)
