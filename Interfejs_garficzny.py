#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from frequency_generator import *
from notes_map import *

window = Tk()

root = ttk.Notebook(window)


tab1 = Frame(root)
tab2 = Frame(root)


root.add(tab1, text="Stroik")
root.add(tab2, text="Akordy")
root.pack(expand=TRUE, fill="both")


def show():
    label.config(text=clicked.get(),)
def play_sound():
    if varA.get() ==1:
        play_note(notes_map['E2'])
    elif varB.get()==1:
        play_note(notes_map['B2'])
    else:
        print('zostala wywolana funkcja play_sound()')

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
A=Checkbutton(tab1, text="A", font=("Consolas", 10), width =3, variable = varA, command = play_sound).pack(side= LEFT)
B=Checkbutton(tab1, text="B", font=("Consolas", 10), width =3, variable = varB, command = play_sound).pack(side= LEFT)
C=Checkbutton(tab1, text="C", font=("Consolas", 10), width =3, variable = varC, command = play_sound).pack(side= LEFT)
D=Checkbutton(tab1, text="D", font=("Consolas", 10), width =3, variable = varD, command = play_sound).pack(side= LEFT)
E=Checkbutton(tab1, text="E", font=("Consolas", 10), width =3, variable = varE, command = play_sound).pack(side= LEFT)
#play_button = Button(tab1, text="Play", command=play_sound).pack()


#play_note(notes_map['E2'])
window.mainloop()


