a = int(input("a \n"))
b = int(input("b \n"))


def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def ppcm(a, b):
    return ((a * b) / pgcd(a, b))


print(ppcm(a, b))
