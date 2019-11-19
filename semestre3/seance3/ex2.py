# −∗−coding :  utf−8−∗−
from floats import floatgui

# 1.  Afficher les doubles
p = 3
emin = -2
emax = 3
for e in range(emin, emax + 1):
    for m in range(2 ** -emin, 2 ** emax):
        x = m * 2 ** (e - p + 1)
        print("(", m, ",", e, ")=", x)

#
# 2. Un systeme  jouet
p = 3
emin = -2
emax = 3
allfloats = floatgui(p, emin, emax)
print("Floats=", allfloats)

# 3. En echelle  logarithmique
allfloats = floatgui(logscale=True)
print("Floats=", allfloats)

# 4. avec les nombres negatifs
allfloats = floatgui(allpositive=False)
print("Floats=", allfloats)

# 5. Avec les denormalises
allfloats = floatgui(withdenormals=True)
print("Floats=", allfloats)
