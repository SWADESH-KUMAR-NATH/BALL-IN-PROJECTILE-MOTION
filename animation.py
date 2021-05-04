def animate(i):
    x, y = traj(i)
    redDot.set_data(x,y)
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, interval=10, frames=np.arange(0.0, 100, .1), blit=True, repeat=False)
plt.show()
