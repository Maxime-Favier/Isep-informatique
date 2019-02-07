eleves = []
classesverif = ["A1", "A2", "A3", "P1", "P2", "I1", "I2"]
groupesverif = ["T1", "T2", "T3", "T4", "T5"]


def tri(T):
    n = len(T)
    for j in range(0, len(T) - 1):
        indiceMin = j
        for k in range(j + 1, len(T)):
            if T[k]["id"] < T[indiceMin]["id"]:
                indiceMin = k
        if indiceMin != j:
            T[j], T[indiceMin] = T[indiceMin], T[j]
    return T


run = True
while run:
    print("\n\n\t\t\x1b[6;30;42mMENU\x1b[0m")
    print("\t1 - Créer un élève\n"
          "\t2 - Modifier un élève\n"
          "\t3 - Supprimer un élève\n"
          "\t4 - Liste d'élèves d'une classe\n"
          "\t5 - Liste d'élèves d'un groupe d'une classe\n"
          "\t6 - Quitter")
    try:
        choix = int(input("Votre Choix? "))
    except ValueError:
        print("\t\t\033[91mEntrez un chiffre\033[0m", "\n")
        continue

    if choix == 1:
        # Création d'un élève
        print("\t\t\x1b[6;30;42mNouvel élève\x1b[0m")
        nom = input("\tNom de l'élève")
        prenom = input("\tPrénom de l'élève")
        classe = input("\tClasse de l'élève")
        groupe = input("\tGroupe de l'élève")
        try:
            id = int(input("\t Numéro de l'élève"))
        except ValueError:
            print("\t\t\033[91mEntrez un chiffre\033[0m", "\n")
            continue
        if classe in classesverif and groupe in groupesverif:
            eleves.append({"id": id, "nom": nom, "prenom": prenom, "classe": classe, "groupe": groupe})
            eleves = tri(eleves)
            # print(eleves)
            print("\t\t\x1b[6;30;42mélève ajouté\x1b[0m")
        else:
            print("\t\t\033[91mInformations incorrectes\033[0m", "\n")
            continue

    elif choix == 2:
        # Modifier un élève
        print("\t\t\x1b[6;30;42mModifier élève\x1b[0m")
        for id, eleve in enumerate(eleves):
            print(id, "-", eleve["id"], eleve["nom"], eleve["prenom"], eleve["classe"], eleve["groupe"])
        try:
            modifid = int(input("\tnum de l'élève à modifier? "))
        except ValueError:
            print("\t\t\033[91mEntrez un chiffre\033[0m", "\n")
            continue
        nom = input("\tNom de l'élève (" + eleves[modifid]["nom"] + ") ")
        prenom = input("\tPrénom de l'élève (" + eleves[modifid]["prenom"] + ") ")
        classe = input("\tClasse de l'élève (" + eleves[modifid]["classe"] + ") ")
        groupe = input("\tGroupe de l'élève (" + eleves[modifid]["groupe"] + ") ")
        try:
            idmo = int(input("\tNuméro de l'élève (" + eleves[modifid]["id"] + ")"))
        except ValueError:
            print("\t\t\033[91mEntrez un chiffre\033[0m", "\n")
            continue
        if classe in classesverif and groupe in groupesverif:
            eleves[modifid] = {"id": idmo, "nom": nom, "prenom": prenom, "classe": classe, "groupe": groupe}
            eleves = tri(eleves)
            print("\t\t\x1b[6;30;42mélève ajouté\x1b[0m")
        else:
            print("\t\t\033[91mInformations incorrectes\033[0m", "\n")
            continue

    elif choix == 3:
        # supprimer un élève
        print("\t\t\x1b[6;30;42mModifier élève\x1b[0m")
        for id, eleve in enumerate(eleves):
            print(id, "-", eleve["id"], eleve["nom"], eleve["prenom"], eleve["classe"], eleve["groupe"])
        try:
            supprid = int(input("\tnum de l'élève à supprimer? "))
        except ValueError:
            print("\t\t\033[91mEntrez un chiffre\033[0m", "\n")
            continue
        del eleves[supprid]

    elif choix == 4:
        # liste d'élèves d'une classe
        print("\t\t\x1b[6;30;42mListe d'une classe\x1b[0m")
        for classe in classesverif:
            print(classe)
        selecclasse = input("Entrez la classe")
        if selecclasse in classesverif:
            print("\t\t\x1b[6;30;42mClasse", selecclasse, "\x1b[0m")
            for eleve in eleves:
                if eleve["classe"] == selecclasse:
                    print("\t", eleve["id"], "-", eleve["nom"], eleve["prenom"])
        else:
            print("\t\t\033[91mCette classe n'existe pas\033[0m", "\n")

    elif choix == 5:
        # liste du groupe dans une classe
        print("\t\t\x1b[6;30;42mListe de groupes\x1b[0m")
        selecclasse = input("Entrez une classe")
        selecgroupe = input("Entrez un groupe (T1, ...., T5)")
        if selecclasse in classesverif and selecgroupe in selecgroupe:
            print("\t\t\x1b[6;30;42mClasse", selecclasse, "groupe", selecgroupe, "\x1b[0m")
            for eleve in eleves:
                if eleve["classe"] == selecclasse and eleve["groupe"] == selecgroupe:
                    print("\t", eleve["id"], "-", eleve["nom"], eleve["prenom"])
        else:
            print("\t\t\033[91mCette classe ou groupe n'existe pas\033[0m", "\n")

    else:
        run = False
