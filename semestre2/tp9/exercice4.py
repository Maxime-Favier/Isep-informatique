produits = {1: (1, "Lait", 2.5), 2: (2, "Eau", 2.0), 3: (3, "Chocolat", 1.5), 4: (4, "Beurre", 4.5)}
cabas = {1: 0, 2: 0, 3: 0, 4: 0}
ca = {"Lait": 0, "Eau": 0, "Chocolat": 0, 'Beurre': 0}

run = True
while run:

    print("\n\n\t\t\x1b[6;30;42mMENU\x1b[0m")
    print("\t1- nouveau client\n"
          "\t2- Info CA\n"
          "\t3- Quitter\n")
    choix = int(input("Votre choix"))

    if choix == 1:
        x = 0
        while x != -1:
            x = int(input("entrez votre produit"))
            if x in produits:
                cabas[x] += 1

            else:
                x = -1
                total = 0
                for j in cabas.items():
                    if j[1] != 0:
                        print(j[0], produits[j[0]][1], "quantité ", j[1], "total=", j[1] * produits[j[0]][2])
                        ca[produits[j[0]][1]] += j[1] * produits[j[0]][2]
                        total += j[1] * produits[j[0]][2]
                print("\t\t*****Total:", total, "€")

    elif choix == 2:
        catot = 0
        for id, item in enumerate(ca.items()):
            print(id +1, item[0], ":", item[1], "euros")
            catot += item[1]
        print("CA total", catot, "€")

    else:
        run = False
