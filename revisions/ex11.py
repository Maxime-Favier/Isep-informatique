n = int(input("entrez un nbr \n"))
paire = 0
impaire = 0
for i in range(0, n + 1):
    if i%2 == 0:
        paire +=1
    else:
        impaire +=1

print("paire", paire)
print("impaire", impaire)
