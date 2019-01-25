repartition = {"O+": 36.5, "O-": 6.5, "A+": 38.2, "A-": 6.8, "B+": 7.7, "B-": 1.4, "AB+": 2.5, "AB-": 0.4}

donneurs = {"O+": ["O+", "A+", "B+", "AB+"], "O-": ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"],
            "A+": ["A+", "AB+"], "A-": ["A+", "A-", "AB+", "AB-"], "B+": ["B+", "AB+"],
            "B-": ["B+", "B-", "AB+", "AB-"], "AB+": ["AB+"], "AB-": ["AB+", "AB-"]}

groupe = input("entrez votre groupe sanguin")
proba = 0

for i in donneurs[groupe]:
    proba += repartition[i]

print(proba)