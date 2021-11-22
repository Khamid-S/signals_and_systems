import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
# from playsound import playsound
# import winsound

# winsound.PlaySound('audio/Project3_v2.wav', winsound.SND_ASYNC) ## windows specific code

data1, sampleRate1 = sf.read('audio/Project3_vtest.wav')

plt.figure(1)
plt.title("Signal project 1")
plt.plot([abs(ele) for ele in data1])

result = np.fft.fft(data1)
plt.figure(2)
plt.title("Signal F transform")


for i in range(0, len(result)-10):
    if abs(result[i]) < 200 and not(abs(result[i-10]) > 300 or abs(result[i+10]) > 300):
        result[i] = 0

plt.plot([abs(ele) for ele in result])


cleanSignal = np.fft.ifft(result)

data2 = []
signalPoints = []
signalCount = 0

el = 0
while el < len(data1)-20000:
    el += 100
    j = 0
    _sum = 0
    while j < sampleRate1:
        j += 1
        _sum += abs(cleanSignal[el])
    if _sum / sampleRate1 > 0.04:
        # print('element found')
        # print(el)
        signalPoints.append(el)
        el += sampleRate1
        signalCount += 1

print(signalPoints)
print(signalCount)

signals = []
fSignals = []


for i in range(0, signalCount):
    fSignals.append((np.fft.fft(cleanSignal[signalPoints[i]:signalPoints[i]+sampleRate1])))
    plt.figure(i+3)
    plt.title("signal " + str(i+1))
    plt.plot([abs(ele) for ele in fSignals[i]])
    print('--------------------------')
    print('signal' + str(i+1))
    for j in range(1, int(len(fSignals[i]) / 2)):
        if abs(fSignals[i][j]) > abs(fSignals[i][j - 1]) and \
                abs(fSignals[i][j]) > abs(fSignals[i][j + 1]) and abs(fSignals[i][j]) > 100:
            print(j)

plt.show()
