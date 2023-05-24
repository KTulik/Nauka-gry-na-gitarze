#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

window = Tk()

root = ttk.Notebook(window)


tab1 = Frame(root)
tab2 = Frame(root)



root.add(tab1, text ="Stroik")
root.add(tab2, text ="Akordy")
root.pack(expand = TRUE, fill="both")