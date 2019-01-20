import sqlite3
import datetime

conn = sqlite3.connect('cours.db')
c = conn.cursor()


def createEvent(prof, dateDebut, dateFin, quota, sujet):
    c.execute("""INSERT INTO cours(prof, dateDebut, dateFin, eleves, quota, name) VALUES(?, ?, ?, "", ?, ?)""",
              (prof, dateDebut, dateFin, quota, sujet))
    print("\x1b[6;30;42m""event created", '\x1b[0m', '\n')
    conn.commit()


def login(username):
    c.execute("""SELECT prof FROM prof WHERE prof = ?""", (username,))
    liste = c.fetchone()
    return liste


def register(username):
    c.execute("""INSERT INTO prof(prof) VALUES (?)""",
              (username,))
    conn.commit()
    print("\x1b[6;30;42m""user created", '\x1b[0m', '\n')


def addstudent(eventid, name):
    c.execute("""SELECT eleves, quota FROM cours WHERE id= ?""", (eventid,))
    event = c.fetchone()
    quota = int(event[1])
    student = event[0].split()
    if quota > len(student):
        student.append(name)
        c.execute("""UPDATE cours SET eleves = ? WHERE id = ?""",
                  (str(student).replace(",", " ").replace("[", "").replace("]", "").replace("'", ""), eventid))
        conn.commit()
        print("\x1b[6;30;42m", "Added !", '\x1b[0m', '\n')
    else:
        print("\033[91m", "formation complète", '\033[0m', "\n")


def getStudentList(eventid):
    c.execute("""SELECT eleves FROM cours WHERE id= ?""", (eventid,))
    event = c.fetchone()
    student = event[0].split()
    for name in student:
        print(name)


def getsujetsprof(username):
    c.execute("""SELECT id, name, dateDebut FROM cours WHERE prof=?""", (username,))
    events = c.fetchall()
    for event in events:
        print(event)


def getsujets():
    c.execute("""SELECT id, name, prof, dateDebut FROM cours""")
    events = c.fetchall()
    for event in events:
        print(event)


# print(datetime.datetime.now())
# createEvent("prof1", datetime.datetime.now(), datetime.datetime.now(), 10)
# addstudent(1, "lol3")
next = 1
while next == 1:

    print("\x1b[6;30;42m", "système de RDV", '\x1b[0m')

    userEnter = input("username? ")
    if userEnter == "admin":
        user = 3
    else:
        out = login(userEnter)
        if out == None:
            user = 2
        else:
            user = 1

    if user == 2:
        exit = 0
        while exit != 1:
            # eleves
            print("1, s'inscrire à un RDV\n"
                  "2, quitter\n")
            choix = int(input('choix?\n'))
            if choix == 1:
                getsujets()
                print("Numero de la formation")
                id = int(input("numero\n"))
                addstudent(id, userEnter)
            else:
                exit = 1

    elif user == 3:
        # admin
        exit = 0
        while exit != 1:
            print("1, Creer un RDV\n"
                  "2, inscrire à un RDV\n"
                  "3, liste d'élèves\n"
                  "4, inscrir un prof\n"
                  "5, quitter")
            choix = int(input('choix?\n'))
            if choix == 1:
                prof = input("nom du prof ")
                sujet = input("sujet ")
                datedebut = input("date de début ")
                datefin = input("date de fin ")
                quota = int(input("quota "))
                createEvent(prof, datedebut, datefin, quota, sujet)
            elif choix == 2:
                getsujets()
                print("Numero de la formation")
                id = int(input("numero\n"))
                addstudent(id, input("username de la personnne"))
            elif choix == 3:
                getsujets()
                print("Numero de la formation")
                id = int(input("numero\n"))
                print("\x1b[6;30;42m", "=" * 10, '\x1b[0m')
                getStudentList(id)
                print("\x1b[6;30;42m", "=" * 10, '\x1b[0m', '\n')
            elif choix == 4:
                register(input("username? "))
            else:
                exit = 1

    elif user == 1:
        # prof
        exit = 0
        while exit != 1:
            print("1, Creer un RDV\n"
                  "2, liste d'élèves\n"
                  "3, quitter\n")
            choix = int(input('choix?\n'))
            if choix == 1:
                sujet = input("sujet ")
                datedebut = input("date de début ")
                datefin = input("date de fin ")
                quota = int(input("quota "))
                createEvent(userEnter, datedebut, datefin, quota, sujet)
            elif choix == 2:
                getsujetsprof(userEnter)
                print("Numero de la formation")
                id = int(input("numero\n"))
                print("\x1b[6;30;42m", "=" * 10, '\x1b[0m')
                getStudentList(id)
                print("\x1b[6;30;42m", "=" * 10, '\x1b[0m', '\n')
            else:
                exit = 1
