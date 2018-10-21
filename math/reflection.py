import math 
import numpy
import csv, time

const = 1.56
data = []
#l = 90
start = time.time()

def angle():
    for l in numpy.arange(0, 181, 1):
        for b in numpy.arange(0, 181, 1):
            angle = math.sin(l)/math.sin(b)

            if angle >= const and angle < 1.57:
                #print('Const = sin(l):',l,'sin(b):',b)
                data.append(('sin(L)=', l, 'sin(B)=',b))
                break
    return data

def write_csv(data):
    with open('sin(l)&sin(b)1.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

angle()
write_csv(data)

print(time.time() - start)