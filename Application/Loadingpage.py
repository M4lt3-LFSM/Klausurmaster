import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

class LoadingScreen:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.app.after(0, lambda: self.app.state('zoomed'))
        self.app.title('Loading Page')

        ###########################################################################################################################
        ################################Positioning and Initilazation GIF##########################################################
        ###########################################################################################################################
        self.file = "Application\\Pictures\\loading.gif"
        self.info = Image.open(self.file)

        self.frames = self.info.n_frames

        self.photoimage_objects = [tk.PhotoImage(file=self.file, format=f"gif -index {i}") for i in range(self.frames)]

        self.gif_label = ctk.CTkLabel(self.app, image="", text="")
        self.gif_label.pack(anchor='center', pady=self.app.winfo_height())

        self.animation(current_frame=0)

        ###########################################################################################################################
        #########################################Termination GIF###################################################################
        ###########################################################################################################################

        ###########################################################################################################################
        ##########################################Timer and Text###################################################################
        ###########################################################################################################################

        # TODO: Abfrage von der Datenbank ob eine Klausur in den nächsten 10 min ansteht (Funktion in DATABASECONNECTOR erstellen)
        # TODO: Limit und Score durch die Werte der Abfrage anpassen

        self.timerlabel = ctk.CTkLabel(self.app, text='Klausur in', font=ctk.CTkFont('Jost', 50))
        self.timerlabel.pack(anchor='sw', padx=self.app.winfo_width() * 2.5)

        self.limit = 20

        # TODO: Abfrage für den Timer: Falls eine Klausur ansteht timer starten ansonsten nächste Seite laden
        klausurTerminated = True

        if klausurTerminated:
            self.startTimer(self.limit)

        self.app.mainloop()

    def animation(self, current_frame=0):
        self.image = self.photoimage_objects[current_frame]
        self.gif_label.configure(image=self.image)
        current_frame = (current_frame + 1) % self.frames
        self.app.after(50, lambda: self.animation(current_frame))

    def startTimer(self, limit):
        pass

def loadLoadingPage():
    loadingPage = LoadingScreen()

if __name__ == "__main__":
    loadLoadingPage()
