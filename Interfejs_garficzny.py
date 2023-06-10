from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from frequency_generator import *
from notes_map import *

window = Tk()

root = ttk.Notebook(window)

tab1 = Frame(root)
tab2 = Frame(root)

root.add(tab1, text="Stroik")
root.add(tab2, text="Akordy")
root.pack(expand=TRUE, fill="both")

tuning_notes = ["E", "A", "D", "G", "B", "E"]

def change_button_text():
    A.config(text=tuning_notes[0])
    B.config(text=tuning_notes[1])
    C.config(text=tuning_notes[2])
    D.config(text=tuning_notes[3])
    E.config(text=tuning_notes[4])
    F.config(text=tuning_notes[5])

def show():
    global tuning_notes
    label.config(text=clicked.get())
    tuning_notes = tunings_map[clicked.get()]
    change_button_text()

def play_sound(note):
    play(notes_map[note])

label = Label(tab1, text=" ")
label.grid(row=0, column=1)

options = [
    "Drop_B",
    "Standard_C",
    "Drop_C",
    "Standard_D",
    "Drop_D",
    "Standard_E"
]

clicked = StringVar()
clicked.set("Wybierz standard")

drop = OptionMenu(tab1, clicked, *options)
drop.grid(row=1, column=1)

button = Button(tab1, text="Zatwierdź standard", command=show)
button.grid(row=2, column=1)

A = Button(tab1, text=tuning_notes[0], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[0]))
B = Button(tab1, text=tuning_notes[1], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[1]))
C = Button(tab1, text=tuning_notes[2], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[2]))
D = Button(tab1, text=tuning_notes[3], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[3]))
E = Button(tab1, text=tuning_notes[4], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[4]))
F = Button(tab1, text=tuning_notes[5], font=("Consolas", 10), width=3, command=lambda: play_sound((tunings_map[clicked.get()])[5]))

A.grid(row=4, column=0)
B.grid(row=5, column=0)
C.grid(row=6, column=0)
D.grid(row=4, column=2)
E.grid(row=5, column=2)
F.grid(row=6, column=2)

# Load image
image = Image.open("image/GuitarHead.png")
photo = ImageTk.PhotoImage(image)
new_height = int(image.size[1] * 0.8)
image = image.resize((image.size[0], new_height), Image.LANCZOS)
guitar_head = Label(tab1, image=photo)
guitar_head.grid(row=4, column=1, rowspan=6, sticky="NS")  # Ustawienie położenia w komórce (0, 0)



root.mainloop()