import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import pressureArr
import heartArr

style.use('fivethirtyeight')
fig = plt.figure()
fig.suptitle('A depenting between heart rate and pressure', fontsize=14)
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('xlabel')

pressureArr.iterr()
heartArr.iterr()

def animate(i):
    pressureData = open('press.txt', 'r').read()
    heartData  = open('array.txt', 'r').read()
    pressureLines = pressureData.split('\n')
    heartLines = heartData.split('\n')`
    xs = []
    ys = []
    for line in pressureLines:
        if len(line) > 1:
            arr = line.split('('or')')
            del(arr[0])
            arr[0].split(')')
            arr2 = arr[0].split(')')
            arr3 = arr2[0].split(',')
            x1 = arr3[0]
            x2 = arr3[1]
            x = (2*int(x1)+int(x2))/3
            print(x)
            ys.append(x)
    for line in heartLines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
    ax.clear()
    ax.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()