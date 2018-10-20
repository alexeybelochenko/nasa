import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import pressureArr


style.use('fivethirtyeight')
fig = plt.figure()
fig.suptitle('A depenting between heart rate and pressure', fontsize=14)
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')

ax.set_xlabel('xlabel')

pressureArr.iterr()
def animate(i):
    graphData = open('press.txt', 'r').read()
    lines = graphData.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            arr = line.split('('or')')
            del(arr[0])
            arr[0].split(')')
            arr2 = arr[0].split(')')
            arrY = arr2[1].split('",')
            arr3 = arr2[0].split(',')
            x1 = arr3[0]
            x2 = arr3[1]
            y = arrY[1]
            x = (2*int(x1)+int(x2))/3
            print(x)
            ys.append(x)
            xs.append(y)
    ax.clear()
    ax.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()