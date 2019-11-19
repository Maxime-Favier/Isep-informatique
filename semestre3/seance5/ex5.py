from numpy import matrix
from numpy.matlib import eye

# 1. matrice de permutation
P = matrix([[3], [0], [2], [1]])
I = eye(4)
print("I=", I)
P = I[P]
print("P=", P)

# 2. Produit P*A
A = matrix(list(range(16)))
A = A.reshape((4, 4))
print("A=", A)
print("P*A=", P * A)

# 3. Tableau de permutation
p = matrix([[0], [2], [1]])
A = matrix([[10, -7, 0], [-3, 2, 6], [5, -1, 5]])
print("A=", A)
print("A[p,:]", A[p,:])

