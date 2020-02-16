import pyaudio
import numpy as np
import pylab
from scipy.io import wavfile
import time
import sys
import seaborn as sns

i=0

x = np.arange(10000)
y = np.random.randn(10000)

global xx
xx = []

def audio():

    FORMAT = pyaudio.paInt16 # We use 16bit format per sample
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024 # 1024bytes of data red from a buffer
    RECORD_SECONDS = 0.1
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True)

    stream.start_stream()
    while timer_run:
        in_data = stream.read(CHUNK)
        audio_data = np.fromstring(in_data, np.int16)
        xx.append(np.mean([abs(x) for x in audio_data]))
        
def ret_noise():
    m=np.mean(xx)
    # print(m)
    xx.clear()
    return m            

timer_run = True

def stop_audio_thread():
    global timer_run
    timer_run = False


if __name__ == '__main__' :
    audio()
