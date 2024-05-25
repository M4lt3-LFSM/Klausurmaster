from tkinter import *
from PIL import ImageTk, Image

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
        self.bg_frame = Image.open('GUI\\Pictures\\background1.png')
        self.bg_panel = Label(self.window)
        self.bg_panel.place(relwidth=1, relheight=1)
        
        self.update_bg_image()
        self.window.bind('<Configure>', self.update_bg_image)

        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405')
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor='center')

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white', bd=5, relief=FLAT)
        self.heading.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('GUI\\Pictures\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.grid(row=1, column=0, rowspan=4, padx=(20, 10))

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('GUI\\Pictures\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.grid(row=1, column=1, pady=(30, 10))

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.grid(row=2, column=1, pady=(10, 30))

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.grid(row=3, column=1, sticky='w', padx=(10, 0), pady=(10, 5))

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.grid(row=4, column=1, padx=(10, 20), pady=(5, 10), sticky='w')

        self.username_icon = Image.open('GUI\\Pictures\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.grid(row=4, column=1, sticky='e')

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.grid(row=5, column=1, sticky='w', padx=(10, 0), pady=(10, 5))

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.grid(row=6, column=1, padx=(10, 20), pady=(5, 10), sticky='w')

        self.password_icon = Image.open('GUI\\Pictures\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.grid(row=6, column=1, sticky='e')

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('GUI\\Pictures\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.grid(row=7, column=1, pady=(20, 10))

        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(relx=0.5, rely=0.5, anchor='center')

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.grid(row=8, column=1, pady=(10, 5), sticky='w', padx=(10, 0))

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.grid(row=9, column=1, pady=(10, 5), sticky='w', padx=(10, 0))

        self.signup_img = ImageTk.PhotoImage(file='GUI\\Pictures\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.grid(row=10, column=1, pady=(5, 20), sticky='w', padx=(10, 0))

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage(file='GUI\\Pictures\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='GUI\\Pictures\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.grid(row=6, column=1, sticky='e', padx=(0, 10))

    def update_bg_image(self, event=None):
        self.bg_frame_resized = self.bg_frame.resize((self.window.winfo_width(), self.window.winfo_height()), Image.LANCZOS)
        self.photo_resized = ImageTk.PhotoImage(self.bg_frame_resized)
        self.bg_panel.config(image=self.photo_resized)
        self.bg_panel.image = self.photo_resized

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
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
