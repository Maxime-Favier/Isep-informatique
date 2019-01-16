# -*- coding: utf-8 -*-
notes = []
somme = 0
for i in range(3):
    notes.append(int(input("entrez une note")))

for note in notes:
    somme += note

if somme/len(notes) >= 10:
    print("validé")
else:
    print("refusé")