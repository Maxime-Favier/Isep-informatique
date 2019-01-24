liste = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]
sortie = {}


def count(lis, x):
    out = 0
    while x in liste:
        index = liste.index(x)
        liste[index] = -1
        out += 1
    return out

for element in liste:

    sortie[element] = count(liste, element)
    print(sortie)

