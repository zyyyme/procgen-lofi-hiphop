from random import choice, randint

# Chord progression generator based on Markov's chain

def progression(key):
    #matrix of initial weights. taken from peter keifer's combinatorics of chord progression for mozart.
    #each row represents starting chord, each column represents next chord
    base_weights = [[0,0.08,0,0.07,0.68,0.06,0.11],
                    [0.37,0,0,0,0.46,0,0.17],
                    [0,0,0,1,0,0,0],
                    [0.42,0.1,0,0,0.39,0,0.09],
                    [0.82,0,0,0.05,0,0.07,0.05],
                    [0.14,0.51,0,0.16,0.05,0,0.14],
                    [0,76,0.01,0,0,0.23,0,0]]

    


    scales = {
        60: [60, 62, 63, 65, 67, 68, 70], # C minor
        62: [62, 64, 65, 67, 69, 70, 72], # D minor
        63: [63, 65, 66, 68, 70, 71, 73], # Eb minor
        65: [65, 67, 68, 70, 72, 73, 75], # F minor
        55: [67, 69, 70, 72, 74, 75, 77], # G minor
        57: [69, 71, 72, 74, 76, 77, 79]  # A minor
    }


    progression = ''
    current_chord = choice([1,3,4,5])
    progression += str(current_chord)

    for i in range(3):
        probabilities = []
        probabilities.extend(base_weights[current_chord-1])
        probabilities.sort(reverse=True)
        
        next_chord = choice(probabilities[0:2])
        while next_chord==0:
            next_chord = choice(probabilities[0:2])
    
        current_chord = base_weights[current_chord-1].index(next_chord) +1
        progression += ' ' + str(current_chord)

    root = scales[key]

    chords = []
    print(progression)
    for chord in progression.split(" "):
        first = root[int(chord)-1]
        second = root[int(chord)-1] + 3
        third = root[int(chord)-1] + 7

        chords.append([first,second,third])

    return chords


if __name__ == '__main__':

    print(progression(65))

