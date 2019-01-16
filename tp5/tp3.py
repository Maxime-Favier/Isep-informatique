def factoriel(x):
    if x == 0:
        return 1
    z = 1
    for i in range(1,x +1):
        #print(i)
        z = z*i
    return z

n = int(input("factoriel"))
print(factoriel(n))