from numpy import matrix
from numpy.linalg import matrix_rank
from pylab import plot, text, xlabel, ylabel, title, axis, show

A = matrix([[1.0, 3.0], [2.0, 4.0]])
print("A=", A)
print("Rank=", matrix_rank(A))

delta = 0.3
plot([0.0, A[0, 0]], [0.0, A[1, 0]] , "r-")
text(A[0, 0]- delta, A[1, 0], "a1")
plot([0.0, A[0, 1]], [0.0, A[1, 1]] , "b--")
text(A[0, 1]+ delta, A[1, 1]- delta, "a2")
xlabel("X1")
ylabel("X2")
title("deux vecteurs linéairement indépendants")
axis([0, 4, 0, 4], "square")
show()

A = matrix([[1.0, -2.0], [2.0, -4.0]])
print("A=", A)
print("Rank=", matrix_rank(A))
delta = 0.3
plot([0.0, A[0, 0]], [0.0, A[1, 0]] , "r-")
text(A[0, 0], A[1, 0]- delta, "a1")
plot([0.0, A[0, 1]], [0.0, A[1, 1]] , "b--")
text(A[0, 1]+ delta, A[1, 1]+ delta, "a2")
xlabel("X1")
ylabel("X2")
title("deux vecteurs linéairement dépendants")
axis([-4, 3, -4, 2], "square")
show()
