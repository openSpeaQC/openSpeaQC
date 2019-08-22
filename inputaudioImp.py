import pyaudio
import wave
import time
import audioop
import struct
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
#Object

p = pyaudio.PyAudio()
print(p.get_default_input_device_info())
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
# for i in range(1):
#     wert=0
while True:
        daten=stream.read(CHUNK)
# # left=audioop.tomono(daten,2,1,0)
# # right=audioop.tomono(daten,2,0,1)
# samples=np.fromstring(daten,dtype=np.int16)
# frames_per_buffer_length=len(samples)/4
# print(frames_per_buffer_length)
samples=np.reshape(samples,(int(frames_per_buffer_length),4))
        print(audioop.rms(daten,2))
        time.sleep(0.01)