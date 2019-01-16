from math import *

def premier(n):
    for i in range(2, n, 1):
        if n % i == 0:
            return False
        else:
            return True


list = []
for i in range(0,int(input("premier \n"))):
    if premier(i):
        list.append(i)

print(list)
