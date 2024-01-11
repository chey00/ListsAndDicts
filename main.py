from datetime import datetime

def setDatetime():
    year = int(input("Geburtsjahr: "))
    month = int(input("Monat: "))
    day = int(input("Tag: "))

    return datetime(year, month, day)

def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["prename"] = input("Vorname: ")
    userObject["lastname"] = input("Nachname: ")
    userObject["e-mail"] = "lord@kelvin.org"
    userObject["password"] = "SehrSicher"
    userObject["valid"] = True
    userObject["birthday"] = setDatetime()

    listOfUserObjects.append(userObject)

# Aufgabe 1 (x Punkte)
# Erstellen Sie eine Funktion printUserObject mit dem Parameter userObject.
# Der Parameter enthält ein dict, welches in der Funktion addUserToList
# definiert wurde.
# Geben Sie alle Keys und Values des dicts in folgener Darstellung aus:
# Vorname: Lord
# Nachname: Kelvin
# ...
# Den Geburtstag des Users geben Sie im folgenden Format aus: yyyy-mm-dd
def printUserObject(userObject): # 1 Punkt
    # Variante 1
    print("Vorname:", userObject["prename"])
    print("Nachname:", userObject["lastname"])
    print("e-mail:", userObject["e-mail"])
    print("password:", userObject["password"])

    date = userObject["birthday"]
    date_as_string = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    print("Geburtstag", date_as_string)

    # Variante 2
    for key in userObject.keys():
        print(key + ":", userObject[key])

def checkValidUsers(listOfUserObjects):
    # Aufgabe 2 (xx Punkten)
    # Implementieren Sie die Rückgabe aller aktiven Benutzer als Liste von Strings.
    # Jeder String hat dabei das Format "Nachname, Vorname".
    # Ein Benutzer ist dann Aktiv, wenn der Value zum Key "valid" True ist.

    pass

# In diesem Bereich nichts ändern!
listOfUserObjects = list() # []

userObject = dict()  # {}
userObject["prename"] = "Hans"
userObject["lastname"] = "Peter"
userObject["e-mail"] = "hans@peter.org"
userObject["password"] = "SehrSicher"
userObject["valid"] = True
userObject["birthday"] = datetime(2023, 12, 24)

listOfUserObjects.append(userObject)

userObject = dict()  # {}
userObject["prename"] = "Franz"
userObject["lastname"] = "Meyer"
userObject["e-mail"] = "franzi@web.de"
userObject["password"] = "aefew!"
userObject["valid"] = True
userObject["birthday"] = datetime(2000, 10, 2)

listOfUserObjects.append(userObject)

# Ab hier können Sie Ihr Programm testen
printUserObject(listOfUserObjects[0])
