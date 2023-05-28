import json


with open('src/notes_frequency_map.json') as file:
    notes_map = json.load(file)

with open('src/chords_notes_map.json') as file:
    chords_map = json.load(file)
    for chord in chords_map:
        for note in range(len(chords_map[chord])):
            chords_map[chord][note] = notes_map[chords_map[chord][note]]
