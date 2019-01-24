liste = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]

out = 0
x = int(input("Entrez la valeur à rechercher"))

while x in liste:
    index = liste.index(x)
    liste[index] = -1
    out += 1

print("Le nombre d’occurrences de", x, "est", out)
