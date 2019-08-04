from midiutil import MIDIFile
from midi2audio import FluidSynth
from generators.rhytm_generator import rhytm_generator

def drum_wav(tempo, instrument,keys):

    notes = [keys["kick"],keys["snare"]]
    track = 0
    channel = 0
    time = 0
    duration = 1
    tempo = tempo
    volume = 127


    midi = MIDIFile(1)

    midi.addTempo(track,time,tempo)

    for note in notes:
        midi.addNote(track, channel,note,time, duration,volume)
        time+=1

    time = 0

    hat_pattern = rhytm_generator()

    for i in range(16):
        # if hat_pattern[i] == 1:
        #     midi.addNote(track,channel,keys["hi-hat"],time,0.125,90)

        if (i) % 4 == 0 and i % 8 != 0 :
            midi.addNote(track,channel,keys["op-hat"],time,0.125,70)
        time+=0.125

    with open('midi/drums.mid', 'wb') as output_file:
        midi.writeFile(output_file)

    fs = FluidSynth(instrument)

    fs.midi_to_audio('midi/drums.mid', 'wav/drums.wav')


