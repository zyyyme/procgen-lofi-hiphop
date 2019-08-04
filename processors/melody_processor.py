from generators.melody_generator import melody_generator
from midiutil import MIDIFile
from midi2audio import FluidSynth

def melody_wav(tempo,key,instrument):
    
    melody = melody_generator(key)
    track = 0
    channel = 0
    time = 0
    duration = 0.5
    tempo = tempo
    volume = 127

    midi = MIDIFile(1)

    midi.addTempo(track,time,tempo)

    for note in melody:
        midi.addNote(track,channel,note,time,duration,volume)
        time+=0.5

    with open('midi/melody.mid', 'wb') as output_file:
        midi.writeFile(output_file)

    fs = FluidSynth(instrument)

    fs.midi_to_audio('midi/melody.mid', 'wav/melody.wav')

if __name__ == "__main__":
    melody_wav(70, 65, 'soundfonts/melodies/sax.sf2')
