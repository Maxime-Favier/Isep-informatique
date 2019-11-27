from quadtx import quadtx, quadgui
from floats import computeDigits
from numpy import zeros
from pylab import plot, xlabel, ylabel, title, show, xscale, yscale


def humps(x):
    y = 1 / ((x - 0.3) ** 2 + 0.01) + 1 / ((x - 0.9) ** 2 + 0.04)
    return y


Q, fcount = quadgui(humps, 0, 1, 1.e-4)
exepected = 35.85832539549867
print("Q=", Q)
print("exepected", exepected)
digit = computeDigits(exepected, Q, 10)
print("digits=", digit)
print("fcount=", fcount)

err = zeros(13)
fcount = zeros(13)
for k in range(13):
    tol = 10**-k
    Q, fcount[k] = quadtx(humps, 0, 1, tol)
    err[k] = abs(Q - exepected)
    ratio = err[k]/tol
    print("%8.0e %7d %13.3e %9.3f" % \
          (tol, fcount[k], err[k], ratio))
plot(fcount, err, "bo")
title("Convergence of quadtx")
xlabel("Number of function calls")
ylabel("Error")
xscale("log")
yscale("log")
show()