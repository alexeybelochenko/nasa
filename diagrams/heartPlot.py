import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import heartArr


style.use('fivethirtyeight')
fig = plt.figure()
fig.suptitle('A depenting between heart rate and time', fontsize=14)
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('axes title')

ax.set_xlabel('xlabel')

heartArr.iterr()
def animate(i):
    graphData = open('array.txt', 'r').read()
    lines = graphData.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(y)
            ys.append(x)
    ax.clear()
    ax.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
