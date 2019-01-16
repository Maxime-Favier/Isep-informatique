# -*- coding: utf-8 -*-

annee = int(input("annee"))

if (annee % 4 == 0) and not(annee % 100 == 0) or (annee % 400 == 0):
    print("bissectile")
else:
    print("non bissectile")