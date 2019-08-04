from random import choice

# stupid pentatonic melody generator
def melody_generator(key):
    scales = {
            60: [60,63,65,67,70,72], # C minor
            62: [62,65,67,69,72,74], # D minor
            63: [63,66,68,70,73,75], # Eb minor
            65: [65,68,70,72,75,77], # F minor
            55: [55,58,60,62,65,67], # G minor
            57: [57,60,62,64,67,69]  # A minor
        }

    melody = []
    melody.append(choice(scales[key]))

    for i in range(1,16):
        note = choice(scales[key])
        while note == melody[i-1]:
            note = choice(scales[key])
        
        melody.append(note)

    return melody

if __name__ == "__main__":
    print(melody_generator(65))