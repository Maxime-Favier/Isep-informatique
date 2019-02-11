run = True
texte = []

while run:
    print("\n\n\t\t\x1b[6;30;42mMENU\x1b[0m")
    print("C → Chargement du fichier\n"
          "A → Ajout d'une ligne à la fin du fichier\n"
          "D → Suppression d’une ligne\n"
          "I → Insertion d’une ligne\n"
          "P → Affichage du fichier\n"
          "S → Sauvegarde du fichier\n"
          "Q → Quitter sans sauvegarder")
    choix = input("Entrez votre choix")

    if choix == "C":
        # Chargement du fichier
        print("\n\n\x1b[6;30;42mOuvrir\x1b[0m")
        file = input("chemin d'acces du fichier")
        try:
            with open(file, "r")as file:
                for line in file:
                    texte.append(line.replace("\n", ""))
        except FileNotFoundError:
            print("\t\t\033[91mLe fichier n'existe pas\033[0m", "\n")
            continue
        print("\x1b[6;30;42mFichier chargé!\x1b[0m")

    elif choix == "A":
        print("\n\n\t\x1b[6;30;42mAjout de ligne\x1b[0m")
        # Ajout d'une ligne à la fin du fichier
        newline = input("entrez une ligne")
        texte.append(newline)
        print("\x1b[6;30;42mLigne ajouté!\x1b[0m")

    elif choix == "D":
        print("\n\n\t\x1b[6;30;42mSuppression\x1b[0m")
        # Suppression d’une ligne
        for id, ligne in enumerate(texte):
            print(id + 1, ligne)
        try:
            delete = int(input("Numéro de la ligne à supprimer")) - 1
        except ValueError:
            continue
        del texte[delete]
        print("\x1b[6;30;42mSupprimé!\x1b[0m")

    elif choix == "I":
        # Insertion d’une ligne
        print("\n\n\t\x1b[6;30;42mInsertion d'une ligne\x1b[0m")
        for id, ligne in enumerate(texte):
            print(id + 1, "-", ligne)
        try:
            insert = int(input("Numéro de la ligne à ajouter")) - 1
        except ValueError:
            continue
        newline = input("entrez le texte")
        # insere le text à la position insert
        texte.insert(insert, newline)
        print("\x1b[6;30;42mAjouté!\x1b[0m")

    elif choix == "P":
        # Affichage du fichier
        print("\n\n\t\x1b[6;30;42mContenu du fichier\x1b[0m")
        for ligne in texte:
            print(ligne)

    elif choix == "S":
        # Sauvegarde du fichier
        print("\n\n\t\x1b[6;30;42mSauvegarder\x1b[0m")
        nom = input("chemin/nom du fichier")
        with open(nom, "w") as file:
            for ligne in texte:
                file.writelines(ligne + "\n")
        print("\n\n\t\x1b[6;30;42mSauvegardé!\x1b[0m")

    elif choix == "Q":
        run = False
