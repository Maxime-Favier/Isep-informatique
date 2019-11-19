# -*- coding: utf-8 -*-

# ex3
b = 2
print("b=", b)
print("type(b)=", type(b))
b *= 2.0
print("b=", b)
print("type(b)=", type(b))
del b
# print(b) # erreur


# ex 4
# Listes
a = [1.0, 2.0, 3.0]  # Create a  l i s t
print("a=", a)
for i, j in enumerate(a):
    print("a[" + str(i) + "] =", j)

print(" len(a)=", len(a))  # Determine  length  of  l i s t
a[1: 3] = [12.0, 13.0]
print(" len(a)=", len(a))


# ex5
# Operateurs  arithmetiques
a = 2.
b = 3.
print("a + b=", a + b)
print("a - b=", a - b)
print("a * b=", a * b)
print("a / b=", a / b)
print("a ^ 2=", a ** 2)
print("a % b", a % b)
a = 2  # Integer
b = 1.99  # Floating  point
print("a > b", a > b)
print("a < b", a < b)
print("a >= b", a >= b)
print("a <= b", a <= b)
print("a == b", a == b)
print("a != b", a != b)


# ex6
a = 1.5
if a < 0.0:
    sign = " negative "
elif a > 0.0:
    sign = "positive"
else:
    sign = "zero"

print("a is ", sign)


# ex7
# Boucle  while
nMax = 5
n = 1
a = []  # Create empty  l i s t
while n < nMax:
    a.append(1.0 / n)  # Append element to list
    # meme chose pour a.append(1/n) et a.append(1.0/ n)
    # [1, 0, 0, 0] pour a.append(1//n) => // = division euclidienne
    n += 1
print(a)

start = 1
stop = 5
step = 2
print("range(stop)=", range(stop))
print("range(start, stop)=", range(start, stop))
print("range(start, stop, step)=", range(start, stop, step))

nMax = 5
a = []  # Create empty  list
for n in range(1, nMax):
    a.append(1 / n)
print(a)


# ex 8
print("abs(−5)=", abs(-5))
print("max([2 ,−2 ,3])= ", max([2, -2, 3]))
print("min([2 ,−2 ,3])= ", min([2, -2, 3]))


# ex9
a = 1234.56789
n = 9876
print("%6d" % n)
print("%4.6f" % a)
print("%1.6e" % a)
