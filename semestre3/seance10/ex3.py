from numpy import diff, array, arange
from interp import splineslopesNotAKnot

x = arange(1, 7)
print(x)
y = array([6., 8., 11., 7., 5., 2.])
T = sum(diff(x) * (y[0:-1] + y[1:]) / 2)
# T = h f(a)*f(b) /2
print("T=")
#D=sum(h**2*(d[1:]−d [0:−1])/12.)
#d = splineslopesNotAKnot(diff(x), )