from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from frequency_generator import *
from notes_map import *
import os

window = Tk()

root = ttk.Notebook(window)

tab1 = Frame(root)
tab2 = Frame(root)

root.add(tab1, text="Stroik")
root.add(tab2, text="Akordy")
root.pack(expand=TRUE, fill="both")

tuning_notes = ["E", "A", "D", "G", "B", "E"]

# adding path of the selected folder
folder = "image"

images = {}

for file_name in os.listdir(folder):
    file_path = os.path.join(folder, file_name)
    if os.path.isfile(file_path):
        images[file_name] = file_path

# Displaying the file dictionary
for file_name, file_path in images.items():
    print(f"File Name: {file_name}, File Path: {file_path}")

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
#def play_chord(index):
    #play(chords_map[chord_options[index]])


def change_image(akord):
    global chord_image
    global chord_photo
    #global chord_index
    if akord in images:
        chord_image = Image.open(images[akord])
        chord_photo = ImageTk.PhotoImage(chord_image)
        chord_new_height = int(chord_image.size[1] * 0.4)
        chord_image = chord_image.resize((chord_image.size[0], chord_new_height), Image.LANCZOS)
        Chord_label.configure(image=chord_photo)
        chord_photo.image = chord_photo
    else:
        print("Brak obrazu dla wybranego akordu!")

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

#load basic chord image
chord_image = Image.open("image/A.png")
chord_photo = ImageTk.PhotoImage(chord_image)
chord_new_height = int(chord_image.size[1] * 0.4)
chord_image = chord_image.resize((chord_image.size[0], chord_new_height), Image.LANCZOS)
Chord_label = Label(tab2, image=chord_photo)
Chord_label.grid(row=1, column=3, rowspan=8, sticky="NS")
#index variable
#chord_index=0

#chord buttons
chordA = Button(tab2, text=chord_options[0], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[0]+".png"))
chordAm = Button(tab2, text=chord_options[1], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[1]+".png"))
chordB = Button(tab2, text=chord_options[2], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[2]+".png"))
chordB7 = Button(tab2, text=chord_options[3], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[3]+".png"))
chordBm = Button(tab2, text=chord_options[4], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[4]+".png"))
chordC = Button(tab2, text=chord_options[5], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[5]+".png"))
chordC7 = Button(tab2, text=chord_options[6], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[6]+".png"))
chordD = Button(tab2, text=chord_options[7], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[7]+".png"))
chordDm = Button(tab2, text=chord_options[8], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[8]+".png"))
chordE = Button(tab2, text=chord_options[9], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[9]+".png"))
chordEm = Button(tab2, text=chord_options[10], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[10]+".png"))
chordFhash = Button(tab2, text=chord_options[11], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[11]+".png"))
chordF = Button(tab2, text=chord_options[12], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[12]+".png"))
chordFm = Button(tab2, text=chord_options[13], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[13]+".png"))
chordG = Button(tab2, text=chord_options[14], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[14]+".png"))
chordG7 = Button(tab2, text=chord_options[15], font=("Consolas", 10), width=3, command=lambda: change_image(chord_options[15]+".png"))
#play_chord button
#play_chord_button = Button(tab2, text="Play", font=("Consolas", 10),command =lambda:play_chord(chord_index))

#buttons arragment
chordA.grid(row=1, column=0)
chordAm.grid(row=1, column=1)
chordB.grid(row=2, column=0)
chordB7.grid(row=2, column=1)
chordBm.grid(row=2, column=2)
chordC.grid(row=3, column=0)
chordC7.grid(row=3, column=1)
chordD.grid(row=4, column=0)
chordDm.grid(row=4, column=1)
chordE.grid(row=5, column=0)
chordEm.grid(row=5, column=1)
chordFhash.grid(row=6, column=0)
chordF.grid(row=6, column=1)
chordFm.grid(row=6, column=2)
chordG.grid(row=7, column=0)
chordG7.grid(row=7, column=1)
#play_chord_button.grid(row=9,column=3)




root.mainloop()