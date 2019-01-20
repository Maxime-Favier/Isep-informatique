import signal
import pickle
import sys

conferancesList = []
profList = []


class Conferance(object):

    def __init__(self, titre, datedebut, datefin, quota, prof):
        self.titre = titre
        self.dateDebut = datedebut
        self.dateFin = datefin
        self.quota = quota
        self.prof = prof
        self.participants = []

    def info(self):
        # print('\x1b[6;30;42m' + self.titre + '\x1b[0m' + '\033[91m ' + self.prof + '\033[0m')
        return '\x1b[6;30;42m' + self.titre + '\x1b[0m' + '\033[91m ' + self.prof + '\033[0m'

    def addeleve(self, username):
        if self.quota >= len(self.participants) + 1:
            self.participants.append(username)
            print('\x1b[6;30;42m' + 'Inscrit !' + '\x1b[0m')
        else:
            print("Conférence victime de son succes!")

    def getprof(self):
        return self.prof

    def getparticipants(self):
        for id, participant in enumerate(self.participants):
            print(str(id) + "-", participant)


class Prof(object):

    def __init__(self, username):
        self.username = username
        # global conferancesList
        self.userconfs = []

    def getusername(self):
        return self.username

    def createconferance(self, titre, dateDebut, dateFin, quota):
        global conferancesList
        conferancesList.append(Conferance(titre, dateDebut, dateFin, quota, self.username))
        print(conferancesList)

    def getlistes(self):
        global conferancesList
        self.userconfs = []
        for conf in conferancesList:
            if conf.getprof() == self.username:
                self.userconfs.append(conf)
        for id, conferance in enumerate(self.userconfs):
            print(str(id) + '-', conferance.info())
        x = int(input("Numéro de la conférence? \n "))
        self.userconfs[x].getparticipants()


class Eleve(object):

    def __init__(self, username):
        self.username = username

    def getconferances(self):
        global conferancesList
        for conf in conferancesList:
            print(conf.info())

    def inscription(self):
        global conferancesList
        for id, conferance in enumerate(conferancesList):
            print(str(id) + '-', conferance.info())
        x = int(input("Numéro de la conférence? \n "))
        conferancesList[x].addeleve(self.username)


def saver(signal, frame):
    with open('conferences.bin', 'wb') as fichier:
        pickleragent = pickle.Pickler(fichier)
        global conferancesList
        pickleragent.dump(conferancesList)

    with open('profs.bin', 'wb') as fichier:
        pickleragent = pickle.Pickler(fichier)
        global profList
        pickleragent.dump(profList)

    sys.exit(0)


def loader():
    with open('conferences.bin','rb') as fichier:
        global conferancesList
        pickleragent = pickle.Unpickler(fichier)
        conferancesList = pickleragent.load()

    with open('profs.bin','rb') as fichier:
        global profList
        pickleragent = pickle.Unpickler(fichier)
        profList = pickleragent.load()


loader()
signal.signal(signal.SIGINT, saver)

run = True
while run:

    prof = False

    user = input("Entrez votre username ")

    for id, prof in enumerate(profList):
        if prof.getusername() == user:
            prof = True
            profid = id
            break

    if prof == True:
        continuer = True
        while continuer:
            print("1- ajouter une conférence\n"
                  "2- avoir une liste\n"
                  "3- Quitter\n")
            choice = int(input("Choix? "))

            if choice == 1:
                titre = input("Titre de la conférence? ")
                datedebut = input("date de début? ")
                datefin = input("date de fin? ")
                quota = int(input("quota? "))
                profList[profid].createconferance(titre, datedebut, datefin, quota)

            elif choice == 2:
                profList[profid].getlistes()

            else:
                continuer = False

    else:
        eleve = Eleve(user)
        continuer = True
        while continuer:
            print("1- S'inscrire\n"
                  "2- Voir les conférences\n"
                  "3- Quitter\n")
            choice = int(input("Choix? "))

            if choice == 1:
                eleve.inscription()

            elif choice == 2:
                eleve.getconferances()

            else:
                continuer = False
