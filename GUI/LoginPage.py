import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

def on_resize(event):
    width, height = event.width, event.height
    print(f"Neue Größe - Breite: {width}, Höhe: {height}")

def login():
    email = email_entry.get()
    password = password_entry.get()
    # Hier können Sie den Login-Prozess implementieren
    print(f"E-Mail: {email}, Passwort: {password}")
    messagebox.showinfo("Login", f"E-Mail: {email}\nPasswort: {password}")

def close_app():
    root.destroy()

def create_gui():
    global email_entry, password_entry

    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    root = ctk.CTk()
    root.title("Klausurmaster - Login")
    root.geometry("600x400")
    root.minsize(600, 400)

    # Grid-Layout verwenden
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    frame = ctk.CTkFrame(root)
    frame.grid(sticky='nsew', padx=20, pady=20)

    # Inneres Layout anpassen
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

    # Überschrift
    heading = ctk.CTkLabel(frame, text="Klausurmaster", font=("Helvetica", 24))
    heading.grid(row=0, column=0, pady=10)

    # E-Mail Eingabefeld mit Platzhalter
    email_var = ctk.StringVar()
    email_var.set("E-Mail")
    email_entry = ctk.CTkEntry(frame, textvariable=email_var, width=300, height=30)
    email_entry.grid(row=1, column=0, padx=10, pady=5)

    def on_click_email(event):
        if email_entry.get() == "E-Mail":
            email_entry.delete(0, tk.END)

    def on_focusout_email(event):
        if email_entry.get() == "":
            email_entry.insert(0, "E-Mail")

    email_entry.bind("<FocusIn>", on_click_email)
    email_entry.bind("<FocusOut>", on_focusout_email)

    # Passwort Eingabefeld mit Platzhalter
    password_var = ctk.StringVar()
    password_var.set("Passwort")
    password_entry = ctk.CTkEntry(frame, textvariable=password_var, show='*', width=300, height=30)
    password_entry.grid(row=2, column=0, padx=10, pady=5)

    def on_click_password(event):
        if password_entry.get() == "Passwort":
            password_entry.delete(0, tk.END)
            password_entry.config(show='*')

    def on_focusout_password(event):
        if password_entry.get() == "":
            password_entry.config(show='*')
            password_entry.insert(0, "Passwort")

    password_entry.bind("<FocusIn>", on_click_password)
    password_entry.bind("<FocusOut>", on_focusout_password)

    # Anmelde-Button
    login_button = ctk.CTkButton(frame, text="Anmelden", command=login, width=100, height=30)
    login_button.grid(row=3, column=0, pady=10)

    # Abschalt-Symbol
    # Hier verwenden wir ein Bild für das Abschalt-Symbol
    power_img = Image.open("GUI\\Pictures\\power_icon.png")  # Stellen Sie sicher, dass das Bild vorhanden ist
    power_img = power_img.resize((30, 30), Image.LANCZOS)
    power_photo = ImageTk.PhotoImage(power_img)

    power_button = ctk.CTkButton(root, image=power_photo, command=close_app, width=30, height=30, fg_color=None)
    power_button.image = power_photo  # Referenz halten
    power_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)

    # Resize-Ereignis behandeln
    root.bind("<Configure>", on_resize)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
