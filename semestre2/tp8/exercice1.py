def afficheInverse(str):
    x = ""
    for i in range(len(str) -1, -1, -1):
        x += str[i]
    print(x)

afficheInverse(input("Saisissez une chaîne"))
