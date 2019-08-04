from pydub import AudioSegment
from random import randint,choice
import glob
import json

from processors.drums_processor import drum_wav
from processors.chords_processor import chords_wav
from processors.melody_processor import melody_wav

keys = [60,62,63,65,55,57]

key = choice(keys)

synths = choice([file for file in glob.glob("soundfonts/synths/*.sf2")])
drums = choice([file for file in glob.glob("soundfonts/drums/*.sf2")])
melodies = choice([file for file in glob.glob("soundfonts/melodies/*.sf2")])

with open('soundfonts/drums/bindings.json', 'r') as json_file:
    data = json.load(json_file)

keys = data[drums[17:-4]]

tempo = randint(65,78)

print(synths)
print(drums)

drum_wav(tempo, drums, keys)
chords_wav(tempo, key, synths)
# melody_wav(tempo,key,melodies)
sfx_vinyl = choice([file for file in glob.glob("sfx/vinyl/*.*")])
sfx_rain = choice([file for file in glob.glob("sfx/rain/*.*")])

print(sfx_vinyl)
print(sfx_rain)

# creating song structure and connecting it together
intro  = AudioSegment.from_file('wav/processed_chords.wav')[:-80]

chords = AudioSegment.from_file('wav/processed_chords.wav')[:-80]
drums = AudioSegment.from_file('wav/drums.wav') * 4 + 6
melody = AudioSegment.from_file('wav/melody.wav') 
sfx_vinyl = AudioSegment.from_file(sfx_vinyl) * 32 - 18
sfx_rain = AudioSegment.from_file(sfx_rain) * 32 - 16

# combined = chords.overlay(melody)

combined = chords.overlay(drums) * 4

# combined = chords * 4

track  = intro + combined

# post fx
track = track.overlay(sfx_vinyl)
track = track.overlay(sfx_rain)
combined = combined.fade_in(1000).fade_out(1000)

track.export('output.wav', format='wav')