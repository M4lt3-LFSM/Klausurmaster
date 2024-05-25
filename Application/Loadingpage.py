import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageSequence
import time

class LoadingScreen(ctk.CTk):
    def __init__(self, countdown_time=(0, 0)):
        super().__init__()
        self.geometry('1166x718')
        self.resizable(1, 1)
        self.state('zoomed')
        self.title('Loading Screen')

        # Hintergrundbild
        self.bg_frame = Image.open('Application/Pictures/background1.png')
        self.bg_panel = ctk.CTkLabel(self, text="")
        self.bg_panel.place(relwidth=1, relheight=1)
        
        self.update_bg_image()
        self.bind('<Configure>', self.update_bg_image)

        # Ladeanimation
        self.gif_path = 'Application/Pictures/loading.gif'  # Pfad zu deinem GIF
        self.gif_label = ctk.CTkLabel(self, text="")
        self.gif_label.place(relx=0.5, rely=0.4, anchor='center')
        self.load_gif()

        # Timer-Label
        self.timer_label = ctk.CTkLabel(self, text="", font=("Helvetica", 24), fg_color="black", text_color="white")
        self.timer_label.place(relx=0.5, rely=0.6, anchor='center')
        
        # Countdown Timer
        self.minutes, self.seconds = countdown_time
        self.total_seconds = self.minutes * 60 + self.seconds
        self.update_timer()

    def update_bg_image(self, event=None):
        self.bg_frame_resized = self.bg_frame.resize((self.winfo_width(), self.winfo_height()), Image.LANCZOS)
        self.photo_resized = ImageTk.PhotoImage(self.bg_frame_resized)
        self.bg_panel.configure(image=self.photo_resized)
        self.bg_panel.image = self.photo_resized

    def load_gif(self):
        self.gif_image = Image.open(self.gif_path)
        self.gif_frames = [ImageTk.PhotoImage(frame.copy().resize((150, 150), Image.LANCZOS)) for frame in ImageSequence.Iterator(self.gif_image)]
        self.gif_frame_index = 0
        self.update_gif()

    def update_gif(self):
        frame = self.gif_frames[self.gif_frame_index]
        self.gif_label.configure(image=frame)
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.gif_frames)
        self.after(100, self.update_gif)  # Aktualisiere das GIF alle 100ms

    def update_timer(self):
        if self.total_seconds >= 0:
            minutes, seconds = divmod(self.total_seconds, 60)
            timer_text = f"Time Remaining: {int(minutes):02}:{int(seconds):02}"
            self.timer_label.configure(text=timer_text)
            self.total_seconds -= 1
            self.after(1000, self.update_timer)  # Timer alle 1000ms aktualisieren
        else:
            self.timer_label.configure(text="Time's up!")

if __name__ == "__main__":
    countdown_time = (1, 30)  # Beispielzeit: 1 Minute und 30 Sekunden
    app = LoadingScreen(countdown_time)
    app.mainloop()
