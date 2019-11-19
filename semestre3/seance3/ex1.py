# 1.  Nombres extremes  : INF ,−INF
print("")
print(" 1. Nombres extremes : INF , −INF")
x = float("inf")
print("x=", x)
print("1+x=", 1 + x)
print("2∗x=", 2 * x)
print("x/2=", x / 2)
print("1/x=", 1 / x)
# x=float( "−i n f " )print( "x=" ,x)print( "1+x=" ,TODO)
x = float("-inf")
print("x=", x)
print("1+x=", 1 + x)
print("2∗x=", 2 * x)
print("x/2=", x / 2)
print("1/x=", 1 / x)

# 2. NAN
print("")
print(" 2. NAN")
x = float("nan")
print("x=", x)
print("1+x=", 1 + x)
print("2∗x=", 2 * x)
print("x/2=", x / 2)
print("1/x=", 1 / x)

# 3. Comment produire NAN ?
print("")
print(" 3. Comment produire NAN?")
x = float("inf")
print("x−x", x - x)
print("0*x", 0 * x)
print("x/x", x / x)

# 4.  Division  par  zero
# Produce a ZeroDivisionError
print("")
print(" 4. Division par zero")
x = +0.0
print("x=", x)
print("1.0/ x=", 1. / x)
x = -0.0
print("x=", x)
print("1.0/ x=", 1. / x)
