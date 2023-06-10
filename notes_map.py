import json

#load notes dictionary from notes_frequency_map.json 
with open('notes_frequency_map.json') as file:
    notes_map = json.load(file)

#load chords dictionary from chords_notes_map.json 
with open('chords_notes_map.json') as file:
    chords_map = json.load(file)
    
    #use notes_map to get chords_map with frequencies
    for chord in chords_map:
        for note in range(len(chords_map[chord])):
            chords_map[chord][note] = notes_map[chords_map[chord][note]]
            
#load guitar tunings dictionary from guitar_tunings.json
with open('guitar_tunings.json') as file:
    tunings_map = json.load(file)
# with open('guitar_tunings.json') as file:
#     tunings_map_frequency = json.load(file)
    
#     #use notes_map to get tunings_map with frequencies
    
#     for tuning in tunings_map_frequency:
#         for note in range(len(tunings_map_frequency[tuning])):
#             tunings_map_frequency[tuning][note] = notes_map[tunings_map_frequency[tuning][note]]