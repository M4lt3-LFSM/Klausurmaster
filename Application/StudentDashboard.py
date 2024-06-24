import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
import os
import json
import Database.DatabaseConnector as DatabaseConnector
import Loadingpage as LoadingPage
import threading
import time

class StudentDashboard:
    def __init__(self):

        self.studentEmail, self.studentPassword = self.loadDataFromJson()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.app.after(0, lambda: self.app.state('zoomed'))
        self.app.title('Student Dashboard')

        #################################################################################################################################
        #####################################Frame für Klausuren#########################################################################
        #################################################################################################################################

        self.terminatedKlausurenFrame = ctk.CTkScrollableFrame(self.app)
        self.terminatedKlausurenFrame.place(anchor = ctk.CENTER, relx = 0.5, rely = 0.55, relwidth = 0.9, relheight = 0.8)

        # Configure grid of terminatedKlausurenFrame to expand the klausurFrame
        #self.terminatedKlausurenFrame.grid_rowconfigure(0, weight=1)
        self.terminatedKlausurenFrame.grid_columnconfigure(0, weight=1)

        #################################################################################################################################
        #####################################Inner Klausuren Frame#######################################################################
        #################################################################################################################################

        
        
        # Placeholder for table header
        self.klausurFrame = ctk.CTkFrame(self.terminatedKlausurenFrame, fg_color='#1c304c')
        self.klausurFrame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        for i in range(4):
            self.klausurFrame.grid_columnconfigure(i, weight=1)

        labelFach = ctk.CTkLabel(self.klausurFrame, text="Fach", anchor="center")
        labelFach.grid(row=0, column=0, pady=20, padx=10, sticky="ew")

        labelLehrer = ctk.CTkLabel(self.klausurFrame, text="Lehrer", anchor="center")
        labelLehrer.grid(row=0, column=1, pady=20, padx=10, sticky="ew")

        labelDauer = ctk.CTkLabel(self.klausurFrame, text="Dauer", anchor="center")
        labelDauer.grid(row=0, column=2, pady=20, padx=10, sticky="ew")

        labelStartzeit = ctk.CTkLabel(self.klausurFrame, text="Startzeit", anchor="center")
        labelStartzeit.grid(row=0, column=3, pady=20, padx=10, sticky="ew")

        # Data to display
        #TODO: data-Abfrage in Databaseconnector
        data = [
            ("Mathematik", "Schmidt", "17:55:57", "2024-06-10 17:55:57"),
            ("Physik", "Müller", "17:55:57", "2024-06-10 17:55:57"),
            ("Chemie", "Weber", "17:55:57", "2024-06-10 17:55:57"),
            ("Biologie", "Fischer", "17:55:57", "2024-06-10 17:55:57"),
            ("Informatik", "Schneider", "17:55:57", "2024-06-10 17:55:57")
        ]

        # Add frames for each row of data
        for index, row in enumerate(data, start=1):
            klausurFrame = ctk.CTkFrame(self.terminatedKlausurenFrame, fg_color='#1c304c')
            klausurFrame.grid(row=index, column=0, padx=10, pady=10, sticky="ew")

            for i in range(4):
                klausurFrame.grid_columnconfigure(i, weight=1)

            labelFach = ctk.CTkLabel(klausurFrame, text=row[0], anchor="center")
            labelFach.grid(row=0, column=0, pady=20, sticky="ew")

            labelLehrer = ctk.CTkLabel(klausurFrame, text=row[1], anchor="center")
            labelLehrer.grid(row=0, column=1, pady=20, sticky="ew")

            labelDauer = ctk.CTkLabel(klausurFrame, text=row[2], anchor="center")
            labelDauer.grid(row=0, column=2, pady=20, sticky="ew")

            labelStartzeit = ctk.CTkLabel(klausurFrame, text=row[3], anchor="center")
            labelStartzeit.grid(row=0, column=3, pady=20, sticky="ew")
        #################################################################################################################################
        #####################################/Inner Klausuren Frame########################################################################
        #################################################################################################################################

        #################################################################################################################################
        #####################################/Frame für Klausuren########################################################################
        #################################################################################################################################

        #################################################################################################################################
        #####################################ShutdwonImage###############################################################################
        #################################################################################################################################

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Pictures")
        shutdownImage = ctk.CTkImage(Image.open(os.path.join(image_path, "power_icon.png")), size=(75, 75))

        shutdownBtn = ctk.CTkButton(self.app, image = shutdownImage, text='', fg_color='transparent', hover = False, cursor = 'hand2', command=lambda: self.closeApplication())
        shutdownBtn.place(anchor = ctk.CENTER, relx = 0.95, rely = 0.075, relwidth = 0.1, relheight = 0.1)

        #################################################################################################################################
        #####################################/ShutdwonImage #############################################################################
        #################################################################################################################################

        #################################################################################################################################
        #####################################Timer Label#############################################################################
        #################################################################################################################################

        self.timerLabel = ctk.CTkLabel(self.app, text = f'Zeit zum automatischen Abmelden: ', font = ctk.CTkFont('Jost', 15))
        self.timerLabel.place(anchor = ctk.CENTER, relx = 0.8, rely = 0.075)
    
        self.timer_thread = threading.Thread(target=self.start_timer)
        self.timer_thread.daemon = True  # This will allow the thread to close when the main window closes
        self.timer_thread.start()

        #################################################################################################################################
        #####################################/Timer label#############################################################################
        #################################################################################################################################

        #################################################################################################################################
        #####################################"Welcome Back Label"########################################################################
        #################################################################################################################################

        welcomeBackLabel = ctk.CTkLabel(self.app, text=f'Willkommen zurück {DatabaseConnector.loadStudentPrename(self.studentEmail)}', font=ctk.CTkFont('Jost', 25))
        welcomeBackLabel.place(anchor = ctk.CENTER, relx = 0.12, rely = 0.075)

        #################################################################################################################################
        ####################################/"Welcome Back Label"########################################################################
        #################################################################################################################################

        self.app.mainloop()

    def closeApplication(self):
        self.app.destroy()

    def start_timer(self):
        total_seconds = 10 * 60  # 10 minutes in seconds
        end_time = time.time() + total_seconds
        
        while total_seconds:
            minutes, seconds = divmod(total_seconds, 60)
            self.timerLabel.configure(text=f"Zeit zum automatischen Abmelden: {minutes:02d}:{seconds:02d}")
            self.app.update()  # Update the GUI
            time.sleep(1)
            total_seconds -= 1
            if DatabaseConnector.checkIfExamInTime(self.studentEmail) == True:
                DatabaseConnector.selectLoginadata(self.studentEmail, self.studentPassword, self.app)
        
        self.timer_label.configure(text=f'Zeit zum automatischen Abmelden: 00:00')
        self.app.destroy()

    def loadDataFromJson(self):
        # Bestimmen des AppData-Verzeichnisses
        appdata_dir = os.getenv('APPDATA')
        if not appdata_dir:
            raise EnvironmentError("AppData directory not found.")
        
        # Pfad zur .json-Datei im AppData-Verzeichnis
        json_file_path = os.path.join(appdata_dir, 'app_parameters.json')
        
        # Überprüfen, ob die Datei existiert
        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"No such file: '{json_file_path}'")
        
        # Lesen der Daten aus der .json-Datei
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Extrahieren der Parameter
        parameter1 = data.get('parameter1')
        parameter2 = data.get('parameter2')
        
        print(f"Parameters loaded from {json_file_path}")
        return parameter1, parameter2

def loadStudentDashboard():
    studentDashboard = StudentDashboard()

if __name__ == "__main__":
    loadStudentDashboard()
