u=100
angle=60
ux=u*np.cos(np.deg2rad(angle))
uy=u*np.sin(np.deg2rad(angle))
t1=0
s=0
TWOPI = 100
elst=0.7
fig,ax=plt.subplots()

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

# for ground-line...
g = np.arange(-250, 2200, 1)
w=0*g
l = plt.plot(g,w)

# for Frame...
Frame=plt.axis([-250, 2200, -50, 550])
redDot, = plt.plot([0], [0], 'ro')
