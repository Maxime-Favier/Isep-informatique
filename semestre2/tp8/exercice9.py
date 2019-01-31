eleves = []
classesverif = ["A1", "A2", "A3", "P1", "P2", "I1", "I2"]
groupesverif = ["T1", "T2", "T3", "T4", "T5"]

run = True
while run:
    print("\n\n\t\t\x1b[6;30;42mMENU\x1b[0m")
    print("\t1 - Créer un élève\n"
          "\t2 - Modifier un élève\n"
          "\t3 - Supprimer un élève\n"
          "\t4 - Liste d'élèves d'une classe\n"
          "\t5 - Liste d'élèves d'un groupe d'une classe\n"
          "\t6 - Quitter")
    choix = int(input("Votre Choix? "))

    if choix == 1:
        # Création d'un élève
        print("\t\t\x1b[6;30;42mNouvel élève\x1b[0m")
        nom = input("\tNom de l'élève")
        prenom = input("\tPrénom de l'élève")
        classe = input("\tClasse de l'élève")
        groupe = input("\tGroupe de l'élève")
        id = len(eleves) + 1
        if classe in classesverif and groupe in groupesverif:
            eleves.append({"id": id, "nom": nom, "prenom": prenom, "classe": classe, "groupe": groupe})
            print("\t\t\x1b[6;30;42mélève ajouté\x1b[0m")
        else:
            print("\t\t\033[91mInformations incorrectes\033[0m", "\n")
            continue

    elif choix == 2:
        # Modifier un élève
        print("\t\t\x1b[6;30;42mModifier élève\x1b[0m")
        for id, eleve in enumerate(eleves):
            print(id, "-", eleve["nom"], eleve["prenom"], eleve["classe"], eleve["groupe"])
        modifid = int(input("\tnum de l'élève à modifier? "))
        nom = input("\tNom de l'élève (" + eleves[modifid]["nom"] + ") ")
        prenom = input("\tPrénom de l'élève (" + eleves[modifid]["prenom"] + ") ")
        classe = input("\tClasse de l'élève (" + eleves[modifid]["classe"] + ") ")
        groupe = input("\tGroupe de l'élève (" + eleves[modifid]["groupe"] + ") ")
        if classe in classesverif and groupe in groupesverif:
            id = eleves[modifid]["id"]
            eleves[modifid] = {"id": id, "nom": nom, "prenom": prenom, "classe": classe, "groupe": groupe}
            print("\t\t\x1b[6;30;42mélève ajouté\x1b[0m")
        else:
            print("\t\t\033[91mInformations incorrectes\033[0m", "\n")
            continue

    elif choix == 3:
        # supprimer un élève
        print("\t\t\x1b[6;30;42mModifier élève\x1b[0m")
        for id, eleve in enumerate(eleves):
            print(id, "-", eleve["nom"], eleve["prenom"], eleve["classe"], eleve["groupe"])
        supprid = int(input("\tnum de l'élève à supprimer? "))
        del eleves[supprid]

    elif choix == 4:
        # liste d'élèves d'une classe
        print("\t\t\x1b[6;30;42mListe d'une classe\x1b[0m")
        for classe in classesverif:
            print(classe)
        selecclasse = input("Entrez la classe")
        if selecclasse in classesverif:
            for eleve in eleves:
                print("\t\t\x1b[6;30;42mClasse", selecclasse, "\x1b[0m")
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
