from random import random

def rhytm_generator():

    drum_pattern = {
        "kick": [0 for i in range(16)],
        "snare": [0 for i in range(16)],
        "hi-hat": [0 for i in range(16)]
    }

    hihat_weights = [0.6,0,0.4,0,0.9,0,0.4,0,0.6,0,0.4,0,0.9,0,0.4,0]

    drum_pattern["kick"][0] = 1
    drum_pattern["snare"][8] = 1

    for i in range(16):
        prob = random()
        if hihat_weights[i] > prob:
            drum_pattern["hi-hat"][i] = 1

    return drum_pattern["hi-hat"]

if __name__ == '__main__':
    print(rhytm_generator())