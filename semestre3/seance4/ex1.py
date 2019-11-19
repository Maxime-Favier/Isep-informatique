# ex 1
from floats import (computeDigits, relativeError)


## Erreur  absolue ,  relative

def computeError(exact, computed, basis):
    abserr = abs(computed - exact)
    relerr = relativeError(exact, computed)
    d = computeDigits(exact, computed, basis)
    print("computed=", computed, ",exact=", exact)
    print("Absolute error : ", abserr)
    print("Relative error : ", relerr)
    print("Correct base−", basis, "digits:", d)


computeError(1., 1., 10)
computeError(1., 1., 2)
computeError(1., 2., 10)
computeError(1., 2., 2)
computeError(1., 1.000001, 10)
computeError(1., 1.000001, 2)
computeError(1e+100, 1.000001e+100, 10)
computeError(1e+100, 1.000001e+100, 2)
computeError(0, 1e-100, 10)
computeError(0, 1e-100, 2)
computeError(1., 1.000001, 10)
computeError(1., 1.000001, 2)
computeError(1e+100, 1.000001e+100, 10)
computeError(1e+100, 1.000001e+100, 2)

a = 1
b = 1.000001
alpha = 1e100
computeError(a, b, 10)
computeError(a * alpha, b * alpha, 10)
