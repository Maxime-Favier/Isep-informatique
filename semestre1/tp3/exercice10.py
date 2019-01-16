# -*- coding: utf-8 -*-

nbr = int(input("nbr"))
out = 1
for i in range(nbr, 0, -1):
    # print(i)
    out = out * i

print(out)