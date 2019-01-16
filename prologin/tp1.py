def arnaque_aerienne0(prix_initial, billets, n):
    arnaqueCompteur = 0
    for prix in billets:
        if prix < prix_initial:
            arnaqueCompteur += 1
    if arnaqueCompteur >= 3:
        print("ARNAQUE !")
    else:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")


prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))
arnaque_aerienne0(prix_initial, billets, n)
