# calcul de delta et des racines
l = float(input("un nombre?\n"))
m = float(input("un nombre?\n"))
n = float(input("un nombre?\n"))

z = m ** 2 - 4 * l * n
if z > 0:
    o = (-m + z ** 0.5) / 2 * l
    p = (-m - z ** 0.5) / 2 * l
    print(o, p)
elif z == 0:
    o = -m / 2 * l
    print(o)
else:
    print("ne sais pas encore")
