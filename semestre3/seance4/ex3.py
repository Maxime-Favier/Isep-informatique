from floats import computeDigits, relativeError, expm1Cond, logCond, log1pCond
from numpy import linspace
from pylab import plot, show, title, xlabel, ylabel, yscale
from math import log, log1p, exp, expm1

x = 1.0 + 1.e-6
c = logCond(x)
print("x=", x, "condition number:", c)

def printLog1pError(x, exact):
    computed = log(1.+x)
    print("x=", x)
    print("    Exact=", exact)
    print("With log(1+", x,")")
    print("    Computed=", computed)
    print("    Relative error=", relativeError(exact, computed))
    print("    Number od signif digits=", computeDigits(exact, computed, 10))
    computed = log1p(x)
    print("with log1p(", x, ")")
    print("    Computed=", computed)
    print("    Relative error=", relativeError(exact, computed))
    print("    Number of signif digits=", computeDigits(exact, computed,10))
    return None

printLog1pError(1.e-10, 9.99999999950000000003e-11)
printLog1pError(1.e-20, 9.99999999999999999995e-21)
# pas d'erreur relative avec log1p

x = linspace(-0.5, 0.5, 1000)
y = log1pCond(x)
title("Condition number of log(1+x)")
xlabel("x")
ylabel("Condition number of Log(1+x)")
plot(x, y, 'r-')
show()