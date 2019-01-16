prix = int(input('prix'))
for i in range(10):
    print("\n")

x = 0
essai = 9
while x != prix:
    x = int(input('quel est le prix?'))
    if x > prix:
        print("moins")
        print("essai restants", essai)
        essai -= 1
    elif x < prix:
        print("plus")
        essai -= 1
        print("essai restants", essai)
    else:
        print("gagné en", 10 - essai, "essais")



