from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Task28")
root.geometry("250x200")

entery = ttk.Entry()
entery.pack()

btn = ttk.Button()
btn.pack(anchor = SE, padx = 15, pady = 15,expand=True)




btn["text"] = "Далее"

btnText = btn["text"]

print(btnText)

root.mainloop()