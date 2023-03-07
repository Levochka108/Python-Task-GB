import tkinter as tk
import customtkinter as ctk


class Program():
    def Main():
        # Modes: system (default), light, dark
        ctk.set_appearance_mode("dark")
        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("blue")

        # create CTk window like you do with the Tk window
        app = ctk.CTk()
        app.geometry(f"{440}x{340}")
        app.title("Task 30")

        # Внутри фоновое окно
        frame = ctk.CTkFrame(master=app)
        frame.pack(pady=10, padx=6, fill="both", expand=True)

        def button_function():
            print("Done!!")

        def button_Exit():
            app.destroy()
            print("Exit Done!")

        # label = ctk.CTkLabel(master=app, text="Login Sustem",
        #                      text_font=("Roboto", 22))
        # label.pack(relx=0.2, rely=0.2, anchor=tk.NW)

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(
            master=app, text="Далее", command=button_function)
        button.place(relx=0.64, rely=0.94, anchor=tk.SW)
        button_Exit = ctk.CTkButton(
            master=app, text="Выход", command=button_Exit)
        button_Exit.place(relx=0.2, rely=0.94, anchor=tk.S)

        app.mainloop()

    Main()
