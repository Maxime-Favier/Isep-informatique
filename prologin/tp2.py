def meli_melo_temporel0(lieux, n, etapes, v):
    # print(lieux)
    # print(n)
    # print(etapes)
    # print(v)
    decalage1 = 0
    decalage2 = 0
    for deplacement in etapes:
        if deplacement["voyageur"] == 1:
            pays = deplacement["destination"]
            for lieu in lieux:
                if lieu["id"] == pays:
                    decalage1 = lieu["decalage"]
                    break
        if deplacement["voyageur"] == 2:
            pays = deplacement["destination"]
            for lieu in lieux:
                if lieu["id"] == pays:
                    decalage2 = lieu["decalage"]
                    break
        print(abs(decalage2 - decalage1))


n = int(input())
liste_p = [None] * n
for i in range(0, n):
    (id, decalage) = list(map(int, input().split()))
    lieux_i = {"id": id, "decalage": decalage}
    liste_p[i] = lieux_i
v = int(input())
liste_e = [None] * v
for j in range(0, v):
    (voyageur, destination) = list(map(int, input().split()))
    etape_i = {"voyageur": voyageur, "destination": destination}
    liste_e[j] = etape_i
meli_melo_temporel0(liste_p, n, liste_e, v)
