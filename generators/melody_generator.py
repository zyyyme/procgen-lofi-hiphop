from random import choice, randint

consonant_intervals =  [3, 4, 5, 7, 8, 9, 12]    

def note_checker(chord, note):
    for step in chord:
        if (step % 12 - note % 12) not in consonant_intervals:
            return False

    return True

# stupid pentatonic melody generator
def melody_generator(key, chords):
    # scales = {
    #         60: [60,63,65,67,70,72], # C minor
    #         62: [62,65,67,69,72,74], # D minor
    #         63: [63,66,68,70,73,75], # Eb minor
    #         65: [65,68,70,72,75,77], # F minor
    #         55: [55,58,60,62,65,67], # G minor
    #         57: [57,60,62,64,67,69]  # A minor
    #     }



    melody = []

    for chord in chords:
        for i in range(2):
            if randint(0,100) > 75:
                melody.append([chord[0]+choice(consonant_intervals)*choice([-1,1]),
                 chord[0]+choice(consonant_intervals)*choice([-1,1])])
            else:
                melody.append([chord[0]+choice(consonant_intervals)*choice([-1,1])])

    return melody



if __name__ == "__main__":
    print(melody_generator(65, [[70, 73, 77], [65, 68, 72], [72, 75, 79], [65, 68, 72]]))