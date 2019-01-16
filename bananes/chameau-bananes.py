tas = [
    {"distance": 0,
     "bananes": 1000}
]

chameau = {
    "distance": 0,
    "nbrbananes":0
}


def marcher(km):
    chameau["distance"] += km
    #print("a", chameau["nbrbananes"] ,"mange", abs(km))
    #chameau["nbrbananes"] -= abs(km)
    chameau["nbrbananes"] = chameau["nbrbananes"] - abs(km)

    if chameau["nbrbananes"] < 0:
        print("plus de nourriture")


def getbananes(bananes):
    for index, ta in enumerate(tas):
        if ta.get("distance") == chameau["distance"]:
            tas[index]["bananes"] -= bananes
            chameau["nbrbananes"] += bananes
            print("prise de", bananes, "bananes dans le tas à", ta.get("distance"))
            if chameau["nbrbananes"] >100:
                print("trop de bannanes")
            break


def addtas(km, bananes):
    if bananes != 0:
        tas.append({"distance": km,
                    "bananes": bananes})
        chameau["nbrbananes"] -= bananes


while True:
    print("le chameau est à", chameau["distance"], "km avec sur son dos", chameau["nbrbananes"], "bananes")
    getbananes(int(input("Prise de bannanes")))
    print("le chameau est à", chameau["distance"], "km avec sur son dos", chameau["nbrbananes"], "bananes")
    print(tas)
    marcher(int(input("distance à parcourir")))
    print("le chameau est à", chameau["distance"], "km avec sur son dos", chameau["nbrbananes"], "bananes")
    addtas(chameau["distance"], int(input("ajouter un tas: nbr de bananes")))
    print(tas)


