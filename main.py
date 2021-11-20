import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from playsound import playsound

# spf = wave.open("audio/Project3_v2.wav", "r")
# for i in range(0,9):
#     data, samplerate = sf.read('audio/Dtmf'+str(i)+'.ogg')
#     print(data)
#     result = np.fft.fft(data)
#     plt.figure(i)
#     plt.title("Signal"+ str(i))
#     plt.plot(result)
#
# plt.show()

#
# data, samplerate = sf.read('audio/Dtmf1.ogg')
# print(data)
# result = np.fft.fft(data)
# res = [abs(ele) for ele in result]
# plt.figure(1)
# plt.title("Signal" + str(1))
# plt.plot(res)
# playsound('audio/Project3_v2.wav')

data1, sampleRate1 = sf.read('audio/Project3_v2.wav')
plt.figure(1)

plt.title("Signal project 1")
plt.plot(data1)

data2 = []

for element in range(44000, len(data1) - 1):
    if data1[element - 22000]>0.05 and data1[element] > 0.05 and data1[element+1] < 0.05:
        data2 = data1[element - 44000: element]
        print(element)
print('===========================')
plt.figure(2)
plt.title('data 2')
plt.plot(data2)
print(len(data2))

result = np.fft.fft(data2)
plt.figure(3)
plt.title("Signal F transform")
# plt.plot(result)
print(len(data1))
# print(sampleRate1)
# for e in range(0, len(result)):
#     if not (697/sampleRate1*len(data1) < e < 1477/sampleRate1*len(data1) or \
#             -697/sampleRate1*len(data1) + len(data1) > e > -1477/sampleRate1*len(data1)+len(data1)):
#         result[e] = 0
plt.plot([abs(ele) for ele in result])
#
# cleanSignal = np.fft.ifft(result)
# plt.figure(3)
# plt.title("Clean signal")
# plt.plot(cleanSignal)


# sf.write("audio/test.wav", np.asarray(cleanSignal, dtype=np.float64), sampleRate1)
print('-------------------------')
# playsound('audio/test.wav')


plt.show()

#
# for i in range(1, int((len(res) - 1) / 2)):
#     if res[i] > res[i - 1] and res[i] > res[i + 1] and res[i] > 100:
#         print('--------------------------------------')
#         print(res[i])
#         print(res[i + 1])
#         print(res[i - 1])
#         print(i)
#         print('--------------------------------------')
