from midiutil import MIDIFile
from random import randint
from generators.progression_generator import  progression
from midi2audio import FluidSynth

from filters.lp_filter import lowpass

def chords_wav(tempo, key, instrument):

    chords = progression(key)
    track = 0
    channel = 0
    time = 0
    duration = 2
    tempo = tempo
    volume = 90

    midi = MIDIFile(1)

    midi.addTempo(track,time,tempo)

    delay = randint(0,1)
    print(delay)

    for chord in chords:
        i = 0
        for note in chord:
            
            midi.addNote(track,channel,note,time+0.05*i*delay,duration, volume)
            i+=1

        time +=2

    with open('midi/chords.mid', 'wb') as output_file:
        midi.writeFile(output_file)

    fs = FluidSynth(instrument)

    fs.midi_to_audio('midi/chords.mid', 'wav/chords.wav')

    lowpass('wav/chords.wav', 'wav/processed_chords.wav', 1000)


    return chords