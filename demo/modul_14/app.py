from tkinter import *

window = Tk()

window.title("Willkommen")
window.geometry('880x600')

lbl = Label(window, text="Eingabe")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():

    res = "Willommen " + txt.get()

    lbl.configure(text= res)

btn = Button(window, text="Klick mich", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()