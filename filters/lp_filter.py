import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib

def lowpass(input_file,output_file,cutOff):

    input_file = input_file
    output_file = output_file

    cutOffFrequency = cutOff


    def running_mean(x, windowSize):
        cumsum = np.cumsum(np.insert(x, 0, 0))
        return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize


    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

        if sample_width == 1:
            dtype = np.uint8 
        elif sample_width == 2:
            dtype = np.int16 
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats.")

        channels = np.frombuffer(raw_bytes, dtype=dtype)

        if interleaved:
            
            channels.shape = (n_frames, n_channels)
            channels = channels.T
        else:
            
            channels.shape = (n_channels, n_frames)

        return channels

    with contextlib.closing(wave.open(input_file,'rb')) as spf:
        sampleRate = spf.getframerate()
        ampWidth = spf.getsampwidth()
        nChannels = spf.getnchannels()
        nFrames = spf.getnframes()

        
        signal = spf.readframes(nFrames*nChannels)
        spf.close()
        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

        
        
        freqRatio = (cutOffFrequency/sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)


        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file = wave.open(output_file, "w")
        wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file.writeframes(filtered.tobytes('C'))
        wav_file.close()

if __name__ == "__main__":
    lowpass("chords.wav", "filtered_chords.wav", 1000)
