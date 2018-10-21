import random
import csv

def pressure_bit():
    pressureArr = []
    dt = 1
    arr = []

    for i in range (1,50):
        pressureArr.append((random.randint(100, 140), random.randint(60,90)))

    with open('../model/data/press.txt', 'w') as f:
        for item in pressureArr:
            writer = csv.writer(f)
            arr.append((str(item),dt))
            dt += 1
            
        writer.writerows(arr)