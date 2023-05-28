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
button = Button(tab1, text="click Me", command=show).pack()

# Create Label
label = Label(tab1, text=" ")
label.pack()
window.mainloop()
