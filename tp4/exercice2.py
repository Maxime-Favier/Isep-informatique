lg = int(input("lg de la regle"))
regle = ""
for i in range(0,lg + 1):
    if i % 10 == 0:
        regle = regle + "|"
    else:
        regle = regle + "-"

print("Voici une regle de", lg, "cm")
print(regle)