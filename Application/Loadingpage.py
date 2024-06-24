import customtkinter as ctk
from PIL import Image, ImageTk  # Use ImageTk for better compatibility with PIL Images
import tkinter as tk
import os
import json
import Database.DatabaseConnector as DatabaseConnector
import StudentDashboard
from datetime import datetime

class LoadingScreen:
    def __init__(self):
        self.studentEmail, self.studentPassword = self.loadDataFromJson()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.app.after(0, self.zoom_window)
        self.app.title('Loading Page')

        self.file = "Application/Pictures/loading.gif"
        self.info = Image.open(self.file)

        self.frames = self.info.n_frames
        self.photoimage_objects = [ImageTk.PhotoImage(file=self.file, format=f"gif -index {i}") for i in range(self.frames)]

        self.gif_label = ctk.CTkLabel(self.app, image=self.photoimage_objects[0], text="")
        self.gif_label.place(anchor=ctk.CENTER, rely=0.3, relx=0.5)

        self.animation(current_frame=0)

        self.timerlabel = ctk.CTkLabel(self.app, text='Klausur in', font=ctk.CTkFont('Jost', 50))
        self.timerlabel.place(anchor=ctk.CENTER, relx=0.4, rely=0.5)

        examTime = DatabaseConnector.checkIfExamInTime(self.studentEmail)

        if examTime is not True:
            self.startTimer(examTime)
        else:
            self.app.after(0, self.terminate_and_load_dashboard)

        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.app.mainloop()

    def zoom_window(self):
        if self.app.winfo_exists():
            self.app.state('zoomed')

    def animation(self, current_frame=0):
        if self.app.winfo_exists():
            self.image = self.photoimage_objects[current_frame]
            self.gif_label.configure(image=self.image)
            current_frame = (current_frame + 1) % self.frames
            self._after_id = self.app.after(50, lambda: self.animation(current_frame))

    def startTimer(self, examTime):
        print(examTime)
        # while examTime-datetime.now() <= 0:
        #    self.timerlabel.config(text=f'Klausur in {examTime-datetime.now()}')

    def loadDataFromJson(self):
        appdata_dir = os.getenv('APPDATA')
        if not appdata_dir:
            raise EnvironmentError("AppData directory not found.")

        json_file_path = os.path.join(appdata_dir, 'app_parameters.json')

        if not os.path.exists(json_file_path):
            raise FileNotFoundError(f"No such file: '{json_file_path}'")

        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        parameter1 = data.get('parameter1')
        parameter2 = data.get('parameter2')

        print(f"Parameters loaded from {json_file_path}")
        return parameter1, parameter2

    def terminate_and_load_dashboard(self):
        if hasattr(self, '_after_id'):
            self.app.after_cancel(self._after_id)
        self.app.destroy()
        StudentDashboard.loadStudentDashboard()

    def on_closing(self):
        if hasattr(self, '_after_id'):
            try:
                self.app.after_cancel(self._after_id)
            except AttributeError:
                pass
        self.app.destroy()

def loadLoadingPage():
    loadingPage = LoadingScreen()

if __name__ == "__main__":
    loadLoadingPage()
