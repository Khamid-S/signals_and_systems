import numpy as np
import soundfile as sf

# from playsound import playsound
# import winsound

# winsound.PlaySound('audio/Project3_v2.wav', winsound.SND_ASYNC) ## windows specific code

phone_number = ''

data1, sampleRate1 = sf.read('audio/Project3_v2.wav')

result = np.fft.fft(data1)
for i in range(0, len(result)-10):
    if abs(result[i]) < 200 and not(abs(result[i-10]) > 300 or abs(result[i+10]) > 300):
        result[i] = 0

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


signals = []
fSignals = []


for i in range(0, signalCount):
    fSignals.append((np.fft.fft(cleanSignal[signalPoints[i]:signalPoints[i]+sampleRate1])))
    low_component = 0
    for j in range(1, int(len(fSignals[i]) / 2)):
        if abs(fSignals[i][j]) > abs(fSignals[i][j - 1]) and \
                abs(fSignals[i][j]) > abs(fSignals[i][j + 1]) and abs(fSignals[i][j]) > 100:
            if j < 1000:
                low_component = j
            if j > 1000:
                if low_component == 697:
                    if j == 1209:
                        phone_number += '1'
                    if j == 1336:
                        phone_number += '2'
                    if j == 1477:
                        phone_number += '3'

                if low_component == 770:
                    if j == 1209:
                        phone_number += '4'
                    if j == 1336:
                        phone_number += '5'
                    if j == 1477:
                        phone_number += '6'

                if low_component == 852:
                    if j == 1209:
                        phone_number += '7'
                    if j == 1336:
                        phone_number += '8'
                    if j == 1477:
                        phone_number += '9'

                if low_component == 941:
                    phone_number += '0'

print('BAD GUY\'S PHONE NUMBER DETECTED!!!')
print('----------------------------------------')
print('phone number is '+phone_number)
