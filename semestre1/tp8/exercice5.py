liste = [2, 65, 42, 53, 27, 2, 42, 27, 2, 53, 53, 53, 65, 21, 27, 53, 2, 53, 65, 27]

x = int(input("Entrez la valeur à supprimer"))
while x in liste:
    del liste[liste.index(x)]
    # liste.remove(x)
print(liste)