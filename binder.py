import json

drums = {
    "drums_808": {
        "kick": 35,
        "snare": 39,
        "hi-hat": 44,
        "op-hat": 46
    },

    "drums_slingerland": {
        "kick": 50,
        "snare": 52,
        "hi-hat": 59,
        "op-hat": 64
    },
}

with open("soundfonts/drums/bindings.json", "w") as f:
    json.dump(drums,f)