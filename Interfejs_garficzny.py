#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

window = Tk()

root = ttk.Notebook(window)


tab1 = Frame(root)
tab2 = Frame(root)


root.add(tab1, text="Stroik")
root.add(tab2, text="Akordy")
root.pack(expand=TRUE, fill="both")


def show():
    label.config(text=clicked.get(),)
def playA():
    print("gram A")
label = Label(tab1, text=" ")
label.pack()


# Dropdown menu options
options = [
    "Standard1",
    "Standard2",
    "Standard3",
    "Standard4",
    "Standard5",
    "Standard6",
    "Standard7"
]
# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Wybierz standard")

# Create Dropdown menu
drop = OptionMenu(tab1, clicked, *options)
drop.pack()


# Create button, it will change label text, we should add a way it impacts play sound function
button = Button(tab1, text="Zarwierdz standard", command=show).pack()

# Create Label


# okienka do zaznaczania z przypisanymi im zmiennymi
varA = IntVar()
varB = IntVar()
varC = IntVar()
varD = IntVar()
varE = IntVar()
A=Checkbutton(tab1, text="A", font=("Consolas", 10), width =3, variable = varA ).pack(side= LEFT)
B=Checkbutton(tab1, text="B", font=("Consolas", 10), width =3, variable = varB).pack(side= LEFT)
C=Checkbutton(tab1, text="C", font=("Consolas", 10), width =3, variable = varC).pack(side= LEFT)
D=Checkbutton(tab1, text="D", font=("Consolas", 10), width =3, variable = varD).pack(side= LEFT)
E=Checkbutton(tab1, text="E", font=("Consolas", 10), width =3, variable = varE).pack(side= LEFT)

window.mainloop()
