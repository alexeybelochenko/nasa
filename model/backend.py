import statistics
import os
from watson_developer_cloud import TextToSpeechV1
from generators import heartArr, pressureArr

pulse = 72
age = 37
mass = 96   
inp = 122/81

heartArr.pulse_bit()
pressureArr.pressure_bit()

def PressureDataGen():
    pressure = []
    pressureData  = open('data/press.txt', 'r').read().split('\n')

    for pressure_b in pressureData:
        if len(pressure_b) > 1:
            arr = pressure_b.split('('or')')
            del(arr[0])
            arr[0].split(')')
            arr2 = arr[0].split(')')
            arr3 = arr2[0].split(',')
            x = arr3[0]
            y = arr3[1]
    
        pressure.append((int(x),int(y)))
    return pressure

def PulseDataGen():
    pulse = []
    heartData  = open('data/pulse.txt', 'r').read().split('\n')
    for line in heartData:
        if len(line) > 1:
            x, _ = line.split(',')
            pulse.append(x)

    return pulse

def speech():
    result = analyse()
    text_to_speech = TextToSpeechV1(
        username='e019c9f5-fea2-4df2-953b-8e412d79b898',
        password='uhOjTp18vJCX',
        url='https://stream.watsonplatform.net/text-to-speech/api'
    )
    with open('voice_data/help.wav', 'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(
                result[1],
                'audio/mp3',
                'en-US_AllisonVoice'
            ).get_result().content)

def analyse():
    pulse_result = PulseDataGen()
    pressure_result = PressureDataGen()

    data = [int(i) for i in pulse_result]
    average = int(statistics.mean(data))
    normal_systolic = 109 + (0.5 * age) + (0.1 * mass)
    normal_diastolic = 63 + (0.1 * age) + (0.15 * mass)
    normal_pressure = round((2*int(normal_systolic)+int(normal_diastolic))/3)
    #Calculate our target zone in the heart rate: (50%-60%)
    target_zone = (int((220-age) * 0.5), int((220-age) * 0.6))
    data = [round(x/y, 1) for x, y in pressure_result]

    short_description = ' Your average pulse {} bit per minute,\n Normal pressure for your body {}/{},\n Expected heart rate zones {},\n Expected pulse {min} - {max} bit per minute'.format(average, int(normal_systolic), int(normal_diastolic), '50% to 60%',min=target_zone[0],max=target_zone[1])

    if pulse > target_zone[1]:
        if inp > normal_pressure:
            advice = "Attention! You have high blood pressure. Try holding your breath for 10 seconds on 3 minutes."
        else:
            if inp < normal_pressure:
                advice = 'It looks like you have psychological instability'
            elif inp > normal_pressure:
                advice = 'Attention! You have a critical overpressure. We insist on returning to the residential unit in order to make follow-up recommendations.'
    else:
        advice = 'Your pulse in normal'

    
    return short_description, advice
        
speech()
result = analyse()
print(result[0])
print(result[1])
os.system('start voice_data/help.wav')