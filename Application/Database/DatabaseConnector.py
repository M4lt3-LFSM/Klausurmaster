import mysql.connector
from mysql.connector import Error
import sys
import os
import hashlib
from datetime import datetime, timedelta
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Loadingpage as Loadingpage
import LoginPage

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
            LoginPage.save_parameters_to_json(email, password)
            login_window.destroy()  # Schließt die Login-Seite
            Loadingpage.loadLoadingPage()
        elif result == "teacher":
            pass
        elif result == "admin":
            pass

    except Error as err:
        print(f"Fehler bei der Abfrage: {err}")

def checkIfExamInTime(studentEmail):
    try:
        current_time = datetime.now()
        ten_minutes_later = current_time + timedelta(minutes=10)

        # SQL-Abfrage, um die nächsten Klausuren für den angegebenen Studenten zu erhalten
        sql_command = ("SELECT datesofexams.dateOfExam, courses.courseID "
                    "FROM datesofexams "
                    "JOIN exams ON exams.dateID = datesofexams.dateID "
                    "JOIN coursesandstudents ON coursesandstudents.courseID = exams.courseID "
                    "JOIN students ON coursesandstudents.studentEmail = students.studentEmail "
                    "JOIN courses ON courses.courseID = exams.courseID "  # Added space here
                    "WHERE students.studentEmail = %s AND datesofexams.dateOfExam BETWEEN %s AND %s")

        values = (studentEmail, current_time, ten_minutes_later)

        klausurmastercursor.execute(sql_command, values)

        result = klausurmastercursor.fetchone()

    except Exception as e:
        result = [datetime.now()]

    result = True
    
    print(result)
    return result

def loadStudentPrename(studentEmail):
    try:
        sql_command = ("SELECT studentPrename from students WHERE studentEmail = %s")

        values = (studentEmail)

        klausurmastercursor.execute(sql_command, values)

        result = klausurmastercursor.fetchone()
        
    except Exception as e:
        result = "Schüler"

    return result

def loadKlausurenForStudentDashbord(studentEmail):
    sql_command = (
            f"SELECT courses.courseName, teachers.teacherLastname, datesofexams.dateOfExam, enddatesofexams.endDateOfExam "
            f"FROM courses "
            f"JOIN exams ON courses.courseID = exams.courseID "
            f"JOIN teachers ON teachers.teacherShorty = courses.teacherShorty "
            f"JOIN coursesandstudents ON courses.courseID = coursesandstudents.courseID "
            f"JOIN datesofexams ON exams.dateID = datesofexams.dateID "
            f"JOIN enddatesofexams ON exams.endDateID = enddatesofexams.endDateID "
            f"WHERE coursesandstudents.studentEmail = %s"
            f"AND datesofexams.dateOfExam > %s"
            f"ORDER BY datesofexams.dateOfExam"
        )

    values = (studentEmail, datetime.now())

    # Daten einfügen
    klausurmastercursor.execute(sql_command, values)

    result = klausurmastercursor.fetchall()

    print("Das Ergebnis ist:")
    print(result)

    data =  []

    for result in result:
        datetime1 = result[2]  # Annahme: Erste Spalte ist datetime_column1
        datetime2 = result[3]  # Annahme: Zweite Spalte ist datetime_column2

    # Konvertiere zu datetime-Objekten, wenn sie nicht bereits datetime-Objekte sind
    if not isinstance(datetime1, datetime):
        datetime1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S")
        
        if not isinstance(datetime2, datetime):
            datetime2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S")

    # Differenz berechnen
    time_difference = datetime2 - datetime1

    data.append([result[0], result[1], time_difference, result[2]])

    return data

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
