import customtkinter as ctk
from AnimatedGIF import * 
from PIL import Image
import os
import tkinter as tk

class LoadingScreen():
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()  # create CTk window like you do with the Tk window
        self.app.after(0, lambda:self.app.state('zoomed'))
        self.app.title('Loading Page')

        
        ###########################################################################################################################
        ################################Positioning and Initilazation GIF##########################################################
        ###########################################################################################################################
        self.file = "Application\\Pictures\\loading.gif"
        self.info = Image.open(self.file)

        self.frames = self.info.n_frames

        self.photoimage_objects = []
        for i in range(self.frames):
            obj = tk.PhotoImage(file=self.file, format=f"gif -index {i}")
            self.photoimage_objects.append(obj)

        self.gif_label = ctk.CTkLabel(self.app, image="", text="")
        self.gif_label.pack(anchor='center', pady=self.app.winfo_height())

        self.animation(current_frame=0)

        ###########################################################################################################################
        #########################################Termination GIF###################################################################
        ###########################################################################################################################

        ###########################################################################################################################
        ##########################################Timer and Text###################################################################
        ###########################################################################################################################
        


        self.app.mainloop()

    def animation(self, current_frame=0):
        global loop
        self.image = self.photoimage_objects[current_frame]

        self.gif_label.configure(image=self.image)
        current_frame = current_frame + 1

        if current_frame == self.frames:
            current_frame = 0

        self.loop = self.app.after(50, lambda: self.animation(current_frame))


def loadLoadingPage():
    loadingPage = LoadingScreen()

if __name__=="__main__":
    loadLoadingPage()