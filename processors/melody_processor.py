from generators.melody_generator import melody_generator
from midiutil import MIDIFile
from midi2audio import FluidSynth

from filters.lp_filter import lowpass

def melody_wav(tempo,key,instrument, chords):
    
    melody = melody_generator(key, chords)
    print(melody)
    track = 0
    channel = 0
    time = 0
    duration = 1
    tempo = tempo
    volume = 127

    midi = MIDIFile(1)

    midi.addTempo(track,time,tempo)

    for note in melody:
        print(note)
        if len(note) == 1:
            midi.addNote(track,channel,note[0],time,duration,volume)
            time+=1
        else:
            print(note[0], note[1])
            midi.addNote(track,channel,note[0],time,duration/2,volume)
            time+=0.5
            midi.addNote(track,channel,note[1],time,duration/2,volume)
            time+=0.5

    with open('midi/melody.mid', 'wb') as output_file:
        midi.writeFile(output_file)

    fs = FluidSynth(instrument)

    fs.midi_to_audio('midi/melody.mid', 'wav/melody.wav')

    lowpass('wav/melody.wav', 'wav/processed_melody.wav', 1200)

if __name__ == "__main__":
    melody_wav(70, 65, 'soundfonts/melodies/sax.sf2', [[72, 75, 79], [73, 76, 80], [67, 70, 74], [65, 68, 72]])
