def saisieMatriceCarree(dimension1 , dimension2):
    matrice = []
    for _ in range(dimension1):
        ligne = []
        for _ in range(dimension2):
            ligne.append(int(input("entrez un nombre")))
        matrice.append(ligne)

    return matrice


def afficheMatriceCarree(matrice):
    for x in matrice:
        print(x)

matrice = saisieMatriceCarree(int(input("dimension 1")), int(input("dimension 2")))
afficheMatriceCarree(matrice)