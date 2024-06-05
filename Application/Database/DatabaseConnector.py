import mysql.connector
from mysql.connector import Error
import sys
import os
import hashlib
import Loadingpage
import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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

def selectLoginadata(email, password, login_window):
    try:
        result = "student"
        
        sql_query = "SELECT studentEmail, studentPassword from students WHERE studentEmail = %s AND studentPassword = %s"
        # TODO: Remove comments from SQL-Statements
        # klausurmastercursor.execute(sql_query, (email,), hashlib.sha256(password.encode()).hexdigest())
        # result = klausurmastercursor.fetchall()

        if result is None:
            sql_query = "SELECT teacherEmail, teacherPassword from teachers WHERE teacherEmail = %s AND teacherPassword = %s"
            # TODO: Remove comments from SQL-Statements
            # klausurmastercursor.execute(sql_query, (email,), hashlib.sha256(password.encode()).hexdigest())
            # result = klausurmastercursor.fetchall()

            if result is None:
                sql_query = "SELECT adminEmail, adminPassword from admins WHERE adminEmail = %s AND adminPassword = %s"
                # TODO: Remove comments from SQL-Statements
                # klausurmastercursor.execute(sql_query, (email,), hashlib.sha256(password.encode()).hexdigest())
                # result = klausurmastercursor.fetchall()

                if result is None:
                    print("Error in LoginData")
                else:
                    result = "admin"
            else:
                result = "teacher"
        else:
            result = "student"

        if result == "student":
            login_window.destroy()  # Schließt die Login-Seite
            Loadingpage.loadLoadingPage()
        elif result == "teacher":
            pass
        elif result == "admin":
            pass

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
def init_Database():
    # TODO: Remove comments from SQL-Statements
    # connectToDatabase()
    if klausurmasterdatabase and klausurmastercursor:
        print("Verbindung erfolgreich")
