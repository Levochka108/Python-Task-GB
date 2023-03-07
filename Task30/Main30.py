from tkinter import *
from tkinter import ttk
import Message


def Main():

    root = Tk()

    root.title("Task28")

    root.geometry("300x200")
    root["bg"] = "gray26"

    def click():
        label["text"] = entery.get()
        print("Команда выполнина!")

    entery = ttk.Entry()
    entery.pack(anchor=NW, padx=6, pady=6)

    label = ttk.Label()
    label.pack(anchor=NW, padx=6, pady=6)

    # Кнопка Выход
    btn = Button(root, bg='#8d8d8d', text="Выход",  fg='white')
    btn.pack(side=LEFT, anchor=SW, padx=15, pady=15)

    # Кнопка далее
    btn_Exit = Button(root, bg='#8d8d8d', text="Далее",
                      fg='white', command=click)
    btn_Exit.pack(side=RIGHT, anchor=SE, padx=15, pady=15)

    root.mainloop()


Main()
