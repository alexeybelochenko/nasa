import random
import csv

def iterr():
    heartArr = []
    dt = 1
    arr = []

    for i in range (1,50):
        heartArr.append(random.randint(60, 68))

    with open('array.txt', 'w') as f:
        for item in heartArr:
            writer = csv.writer(f)
            arr.append((str(item),dt))
            dt += 1
            
        writer.writerows(arr)
