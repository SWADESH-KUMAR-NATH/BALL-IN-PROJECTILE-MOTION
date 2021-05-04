import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
u=100
angle=60
t1=0
s=0
elst=0.7
ux=u*np.cos(np.deg2rad(angle))
uy=u*np.sin(np.deg2rad(angle))
def traj(t):
    global ux,uy,t1,s
    y=uy*(t-t1)-.5*9.8*((t-t1)**2)
    if y>0:
        pass
    elif y<0:
        y=0
        s += ux * (t - t1)
        t1=t
        uy=uy*elst
        ux=ux*elst
    x=s+ux*(t-t1)
    #print(t, ' //// ', t1, ' //// ', uy, ' //// ', x, ' //// ', y)
    return x,y

def init():
    ax.set_xlim(-200,2200)
    ax.set_ylim(-200,400)
    return ln,

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [],"ro")

# # for ground-line...
g = np.arange(-250, 2200, 1)
w=0*g
l = plt.plot(g,w)

def update(frame):
    x,y=traj(frame)
    #print(frame,' //// ',t1,' //// ',u,' //// ',y)
    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 3000, 5000),init_func=init, interval=20, blit=True)
plt.show()
