from tkinter import *
from PIL import ImageTk, Image
import Database.DatabaseConnector as DatabaseConnector
import Loadingpage
import os
import json

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(1, 1)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('Application\\Pictures\\background1.png')
        self.bg_panel = Label(self.window)
        self.bg_panel.place(relwidth=1, relheight=1)
        
        self.update_bg_image()
        self.window.bind('<Configure>', self.update_bg_image)

        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405')
        self.lgn_frame.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.8, anchor='center')

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.grid(row=0, column=0, columnspan=2, pady=(30, 10), sticky='n')

        # ========================================================================
        # ============ Left Side Image ===========================================
        # ========================================================================
        self.side_image = Image.open('Application\\Pictures\\vector.png')
        self.side_image_label = Label(self.lgn_frame, bg='#040405')
        self.side_image_label.grid(row=1, column=0, rowspan=4, padx=(20, 10), sticky='nw')
        
        self.sign_in_image = Image.open('Application\\Pictures\\hyy.png')
        self.sign_in_image_label = Label(self.lgn_frame, bg='#040405')
        self.sign_in_image_label.grid(row=1, column=1, pady=(30, 10), sticky='n')
        
        self.lgn_button = Image.open('Application\\Pictures\\btn1.png')
        self.lgn_button_label = Label(self.lgn_frame, bg='#040405')
        self.lgn_button_label.grid(row=7, column=1, pady=(20, 10), sticky='n')

        self.window.after(100, self.update_side_image)
        self.window.after(100, self.update_sign_in_image)
        self.window.after(100, self.update_login_button)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.grid(row=2, column=1, pady=(10, 30), sticky='n')

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.grid(row=3, column=1, sticky='w', padx=(10, 0), pady=(10, 5))

        self.username_entry = Entry(self.lgn_frame, highlightthickness=2, highlightbackground="#4f4e4d", relief=FLAT, bg="#000000", fg="#ffffff",
                                    font=("yu gothic ui", 16, "bold"), insertbackground='#6b6a69', width=25)
        self.username_entry.grid(row=4, column=1, padx=(10, 20), pady=(5, 10), sticky='w')

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.grid(row=5, column=1, sticky='w', padx=(10, 0), pady=(10, 5))

        self.password_entry = Entry(self.lgn_frame, highlightthickness=2, highlightbackground="#4f4e4d", relief=FLAT, bg="#000000", fg="#ffffff",
                                    font=("yu gothic ui", 16, "bold"), show="*", insertbackground='#6b6a69', width=25)
        self.password_entry.grid(row=6, column=1, padx=(10, 20), pady=(5, 10), sticky='w')

        # ============================login button================================
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.login_action)
        self.login.place(relx=0.5, rely=0.5, anchor='center')

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage(file='Application\\Pictures\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='Application\\Pictures\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.grid(row=6, column=1, sticky='e', padx=(0, 10))

    def login_action(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        DatabaseConnector.selectLoginadata(email, password, self.window)

    def update_bg_image(self, event=None):
        self.bg_frame_resized = self.bg_frame.resize((self.window.winfo_width(), self.window.winfo_height()), Image.LANCZOS)
        self.photo_resized = ImageTk.PhotoImage(self.bg_frame_resized)
        self.bg_panel.config(image=self.photo_resized)
        self.bg_panel.image = self.photo_resized

    def update_side_image(self):
        if self.lgn_frame.winfo_width() > 0 and self.lgn_frame.winfo_height() > 0:
            side_image_resized = self.side_image.resize((int(self.lgn_frame.winfo_width() * 0.3), int(self.lgn_frame.winfo_height() * 0.5)), Image.LANCZOS)
            photo = ImageTk.PhotoImage(side_image_resized)
            self.side_image_label.config(image=photo)
            self.side_image_label.image = photo

    def update_sign_in_image(self):
        if self.lgn_frame.winfo_width() > 0 and self.lgn_frame.winfo_height() > 0:
            sign_in_image_resized = ImageTk.PhotoImage(self.sign_in_image)
            self.sign_in_image_label.config(image=sign_in_image_resized)
            self.sign_in_image_label.image = sign_in_image_resized

    def update_login_button(self):
        if self.lgn_frame.winfo_width() > 0 and self.lgn_frame.winfo_height() > 0:
            lgn_button_resized = self.lgn_button.resize((int(self.lgn_frame.winfo_width() * 0.5), int(self.lgn_frame.winfo_height() * 0.1)), Image.LANCZOS)
            photo = ImageTk.PhotoImage(lgn_button_resized)
            self.lgn_button_label.config(image=photo)
            self.lgn_button_label.image = photo

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.grid(row=6, column=1, sticky='e', padx=(0, 10))
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.grid(row=6, column=1, sticky='e', padx=(0, 10))
        self.password_entry.config(show='*')

def page():
    window = Tk()
    login_page = LoginPage(window)
    window.mainloop()

def save_parameters_to_json(userEmail, userPassword):
    # Bestimmen des AppData-Verzeichnisses
    appdata_dir = os.getenv('APPDATA')
    if not appdata_dir:
        raise EnvironmentError("AppData directory not found.")
    
    # Pfad zur .json-Datei im AppData-Verzeichnis
    json_file_path = os.path.join(appdata_dir, 'app_parameters.json')
    
    # Daten in ein Dictionary packen
    data = {
        'parameter1': userEmail,
        'parameter2': userPassword
    }
    
    # Schreiben oder Überschreiben der Daten in der .json-Datei
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Parameters saved to {json_file_path}")

if __name__ == '__main__':
    DatabaseConnector.init_Database()
    page()
