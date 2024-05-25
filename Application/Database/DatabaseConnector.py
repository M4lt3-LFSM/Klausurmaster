import mysql.connector
from mysql.connector import Error

# Globale Variablen für Datenbankverbindung und Cursor
klausurmasterdatabase = None
klausurmastercursor = None

# Methoden
def connectToDatabase():
    global klausurmasterdatabase, klausurmastercursor
    try:
        klausurmasterdatabase = mysql.connector.connect(
            host='localhost',
            user='root',
            password='qULQ3gBcTnMwzXyoiSCtRYLzP',
            database='klausurmaster'
        )

        klausurmastercursor = klausurmasterdatabase.cursor()
        print("Verbindung zur Datenbank erfolgreich hergestellt.")

    except Error as err:
        print(f"Fehler bei der Verbindung zur Datenbank: {err}")

def selectLoginadata(email, password):
    try:
        print(email, password)
    except Error as err:
        print(f"Fehler bei der Abfrage: {err}")

def closeConnection():
    try:
        if klausurmastercursor:
            klausurmastercursor.close()
            print("Cursor erfolgreich geschlossen.")
        if klausurmasterdatabase:
            klausurmasterdatabase.close()
            print("Datenbankverbindung erfolgreich geschlossen.")

    except Error as err:
        print(f"Fehler beim Schließen der Verbindung: {err}")

# ScriptInitialisierung
if __name__ == "__main__":
    #connectToDatabase()
    if klausurmasterdatabase and klausurmastercursor:
        print ("Verbindung erfolgreich")
