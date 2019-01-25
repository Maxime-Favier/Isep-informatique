taux = (80, 60, 50, 30, 20)

valeur = int(input("valeur initiale de l'immobilisation"))

for annee in range(0, 5):
    ammortissement = (valeur * taux[annee]) / 100
    net = valeur - ammortissement
    print("valeur brute", valeur, "\t taux", taux[annee], "\t ammortisement", ammortissement, "\t valeur net", net )
    valeur = net
