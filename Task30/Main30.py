import tkinter as tk
import customtkinter as ctk
import os


class Program():
    def Main():
        # Modes: system (default), light, dark
        ctk.set_appearance_mode("DARK")
        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("blue")

        # create CTk window like you do with the Tk window
        app = ctk.CTk()
        app.geometry(f"{480}x{420}")
        app.title("Task 30")

        # Внутри фоновая область в окне
        frame_1 = ctk.CTkFrame(master=app)
        frame_1.pack(pady=25, padx=10, fill="both", expand=True)

        # тесет в нутри фоногвой области в окне
        text_1 = ctk.CTkTextbox(master=frame_1, width=444,
                                height=100, font=("Times", 14))
        text_1.pack(pady=10, padx=10)
        text_temp = f"Задача 30:\n\
        Заполните массив элементами арифметической прогрессии.\
        Её первый элемент, разность и количество элементов нужно ввестис клавиатуры.\n\
        Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки."
        text_1.insert("0.0", text_temp)

        label = ctk.CTkLabel(
            master=frame_1, text="Введите элементы", font=("Times", 20))
        label.pack(pady=12, padx=10)

        # Поля ввода текста
        entry_1 = ctk.CTkEntry(
            master=frame_1, placeholder_text="Ввод >", font=("Times", 14))
        entry_1.pack(pady=1, padx=1)
        entry_2 = ctk.CTkEntry(
            master=frame_1, placeholder_text="Ввод >", font=("Times", 14))
        entry_2.pack(pady=2, padx=2)
        entry_3 = ctk.CTkEntry(
            master=frame_1, placeholder_text="Ввод >", font=("Times", 14))
        entry_3.pack(pady=3, padx=3)

        label = ctk.CTkLabel(
            master=frame_1, text="*Для получения ответа нажать Далее.", font=("Times", 11))
        label.pack(pady=10, padx=20)

        def button_function():
            value1 = 0
            value2 = 0
            value3 = 0
            value1 = int(entry_1.get())
            value2 = int(entry_2.get())
            value3 = int(entry_3.get())
            arr = [value1 + (i-1)*value2 for i in range(1, value3 + 1)]
            print(f"Done!!")
            print(arr)

        def button_Exit():
            app.destroy()
            print("Exit Done!")

        # Use CTkButton instead of tkinter Button
        button = ctk.CTkButton(
            master=frame_1, text="Далее", font=("Times", 14),  command=button_function)
        button.place(relx=0.64, rely=0.94, anchor=tk.SW)
        button_Exit = ctk.CTkButton(
            master=frame_1, text="Выход", font=("Times", 14), command=button_Exit)
        button_Exit.place(relx=0.2, rely=0.94, anchor=tk.S)

        app.mainloop()

    Main()
