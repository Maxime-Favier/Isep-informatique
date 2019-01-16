# -*- coding: utf-8 -*-

nbr = int(input("nbr premier"))

for i in range(2, nbr):
    if nbr % i == 0:
        print("non premier")
        break
    if i == nbr -1:
        print("premier")
        break

