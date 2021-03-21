import pyaudio
import numpy as np

maxValue = 2**16
bars = 140
p=pyaudio.PyAudio()
i=0

for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

stream=p.open(format=pyaudio.paInt16,channels=2,rate=44100,
              input=True,input_device_index = 2, frames_per_buffer=1024)

# while i<200:

#     data = np.fromstring(stream.read(1024),dtype=np.int16)
#     dataL = data[0::2]
#     dataR = data[1::2]
#     print(dataR)
#     peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
#     peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
#     print(peakR)
#     # lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
#     rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
#     # print("L=[%s]\tR=[%s]"%(lString, rString))
#     print(rString)
#     i+=1