liste = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]
sortie = {}
noduplic = []


def count(lis, x):
    out = 0
    while x in liste:
        index = liste.index(x)
        liste[index] = -1
        out += 1
    return out


# liste sans duplica
for x in liste:
    if x not in noduplic:
        noduplic.append(x)

for element in noduplic:
    sortie[element] = count(liste, element)

print(sortie)
