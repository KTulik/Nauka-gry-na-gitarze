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
    
def show_chord():
    
    global chord_image
    global chord_photo
    
    choose_chord_label.config(text=clicked_chord.get())
    chord_image = Image.open(chord_image_map[clicked_chord.get()])
    chord_photo = ImageTk.PhotoImage(chord_image)
    chord_new_height = int(chord_image.size[1] * 0.4)
    chord_image = chord_image.resize((chord_image.size[0], chord_new_height), Image.LANCZOS)
    chord_label = Label(tab2, image=chord_photo)
    chord_label.grid(row=3, column=0, rowspan=6, sticky="NS")
    
def play_chord():
    play(chords_map[clicked_chord.get()], 8, 1, "down")
        
# Stroik

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

A.grid(row=6, column=0)
B.grid(row=5, column=0)
C.grid(row=4, column=0)
D.grid(row=4, column=2)
E.grid(row=5, column=2)
F.grid(row=6, column=2)

# # Load image
image = Image.open("image/GuitarHead.png")
photo = ImageTk.PhotoImage(image)
new_height = int(image.size[1] * 0.8)
image = image.resize((image.size[0], new_height), Image.LANCZOS)
guitar_head = Label(tab1, image=photo)
guitar_head.grid(row=4, column=1, rowspan=6, sticky="NS")

#akordy

choose_chord_label = Label(tab2, text =" ")
choose_chord_label.grid(row = 0, column = 0)

chord_options = [
    "A",
    "Am",
    "B",
    "B7",
    "Bm",
    "C",
    "C7",
    "D",
    "Dm",
    "E",
    "Em",
    "F",
    "Fm",
    "F#m",
    "G",
    "G7"
]

clicked_chord = StringVar()
clicked_chord.set("Wybierz akord")

chord_drop = OptionMenu(tab2, clicked_chord, *chord_options)
chord_drop.grid(row = 1, column = 0)

chord_button = Button(tab2, text="Zatwierdź akord", command = show_chord)
chord_button.grid(row = 2, column = 0)

chord_play_button = Button(tab2, text = "Zagraj akord", command = play_chord)
chord_play_button.grid(row = 10, column = 0)

root.mainloop()