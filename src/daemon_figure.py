import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import os

dpi=72
fig=plt.figure(1,figsize=(1500/dpi,800/dpi),dpi=dpi,frameon=False)
ax1=fig.add_axes([0,0,1,1])
fig.set_facecolor('xkcd:salmon')
fig.set_facecolor((1.0, 0.47, 0.42))
img = mpimg.imread(f"{os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'resources', ))}/image.jpeg")
imgplot=ax1.imshow(img,aspect=.9)

x=np.linspace(0,np.pi*10,300)

ax2=fig.add_axes([0.7,0.7,0.3,0.3],frame_on=False)
img2=img.copy()
# img2[:,:,0]=img2[:,:,1]=img2[:,:,2]=.6*img[:,:,0]+.3*img[:,:,1]+.1*img[:,:,2]
img2[:,:,0]=img2[:,:,1]=img2[:,:,2]=np.dot(img2,[.5,.3,.2])
ax2.set_facecolor((1.0, 0.47, 0.42))
ax2.imshow(img2, aspect='equal',extent = [0, 15, 0, 10])


ax1.tick_params(axis='both',bottom=False,left=False,labelleft=False, labelbottom=False)
ax2.tick_params(axis='both',bottom=False,left=False,labelleft=False, labelbottom=False)


from matplotlib.animation import FuncAnimation



#________________________________
y_new = np.sin(2 * np.pi * x)
ax3=fig.add_axes([0,0.2,1,0.1],frame_on=False)
ax3.tick_params(axis='both',bottom=False,left=False,labelleft=False, labelbottom=False)
# Plot a sine wave using time and amplitude obtained for the sine wave

# ax3.plot(x,y_new)
# plt.show()

#______________________
# initializing a line variable
line, = ax3.plot([], [], lw = 4)

# data which the line will
# contain (x, y)
def init():
	line.set_data([], [])
	return line,

def animate(i):
	x = np.linspace(0, 2*np.pi, 500)

	# plots a sine graph
	y = np.sin(2 * np.pi * (x - 0.01 * i))
	line.set_data(x, y)
	
	return line,

anim = FuncAnimation(fig, animate, init_func = init,
					frames = 200, interval = 20, blit = True)


# plt.text(0,0,"DAEMON",bbox=dict(fill=False, edgecolor='red', linewidth=2),fontsize=38, size=50)

fig.savefig('plot.jpeg',dpi=dpi)
anim.save('continuousSineWave.gif', fps = 30)



# plt.show()

