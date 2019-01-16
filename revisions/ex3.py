jour = int(input("jour? \n"))
mois = int(input("mois? \n"))
annee = int(input("annee? \n"))

if mois >= 3:
    j = (23 * mois // 9 + jour + 4 + annee + annee // 4 - annee // 100 + annee // 400 - 2) % 7
else:
    j = (23 * mois // 9 + jour + 4 + annee + (annee - 1) // 4 - (annee - 1) // 100 + (annee - 1) // 400) % 7

if j == 0:
    print("dimanche", jour,"/", mois, "/", annee)
elif j == 1:
    print("lundi",jour,"/", mois, "/", annee)
elif j == 2:
    print("mardi",jour,"/", mois, "/", annee)
elif j == 3:
    print("mercredi", jour,"/", mois, "/", annee)
elif j == 4:
    print("jeudi", jour,"/", mois, "/", annee)
elif j == 4:
    print("vendredi", jour,"/", mois, "/", annee)
elif j == 5:
    print("samedi", jour,"/", mois, "/", annee)
elif j == 6:
    print("dimanche", jour,"/", mois, "/", annee)
