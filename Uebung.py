from datetime import datetime
def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["username"] = "frank.meyer"
    userObject["password"] = "SehrSicher"
    userObject["valid"] = True
    userObject["passwordChanged"] = datetime(2001,2,21)
    userObject["e-mail"] = "lord@kelvin.org"

    listOfUserObjects.append(userObject)

    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList?

    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss.

    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit.

# In dem folgenden Bereich nehmen Sie keine Änderungen vor!
# Testdaten:
userList = list()

user = dict()
user["username"] = "peter.meyer"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "peter@web.de"

user = dict()
user["username"] = "franz.huber"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "hubi@gmx.de"

user = dict()
user["username"] = "julia.meyer"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "jule@meyer.de"


# Ab hier können Sie Ihre Lösungen testen:
print("Viel Erfolg!")
