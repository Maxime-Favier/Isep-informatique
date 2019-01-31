def saisieMatriceCarree(dimension):
    matrice = []
    for _ in range(dimension):
        ligne = []
        for _ in range(dimension):
            ligne.append(int(input("entrez un nombre")))
        matrice.append(ligne)

    return matrice


def afficheMatriceCarree(matrice):
    for x in matrice:
        print(x)

matrice = saisieMatriceCarree(2)
afficheMatriceCarree(matrice)