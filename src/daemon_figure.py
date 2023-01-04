import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

# Set Background Color and dpi and First Layer
plt.rcParams["axes.facecolor"] = "red"

dpi = 100
fig = plt.figure(1, figsize=(3024/dpi, 1632/dpi), dpi=dpi)

ax = fig.add_axes([0, 0, 1, 1])
ax.tick_params(axis='both', bottom=False, left=False,
               labelleft=False, labelbottom=False)
# Read Image and Show it in Second Layer
img = mpimg.imread(
    f"{os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'resources', ))}/image.jpeg")
ax1 = fig.add_axes([0.1, 0.1, .8, .8])
ax1.tick_params(axis='both', bottom=False, left=False,
                labelleft=False, labelbottom=False)
imgplot = ax1.imshow(img, aspect=.5)

# Convert Image to gray and Show it in Third Layer
img2 = img.copy()
img2[:, :, 0] = img2[:, :, 1] = img2[:, :, 2] = np.dot(img2, [.8, .4, 0.3])
ax2 = fig.add_axes([0.6, 0.6, 0.42, 0.4])
ax2.tick_params(axis='both', bottom=False, left=False,
                labelleft=False, labelbottom=False)
ax2.imshow(img2, cmap='gray', aspect=.5)

# Prepairing for Sine Wave (set Forth Layer)
ax3 = fig.add_axes([0.104, 0.3, .794, 0.05], frame_on=False)
ax3.tick_params(axis='both', bottom=False, left=False,
                labelleft=False, labelbottom=False)
# creating a plot
lines_plotted = ax3.plot([], color='black', linewidth=10)

# putting limits on x, y since it is sin function
plt.xlim(0, 2*np.pi)
plt.ylim(-1.1, 1.1)

# initialising: x from 0 to 2∏
x = np.linspace(0, 2*np.pi, 1000)
y = 0
line_plotted = lines_plotted[0]
# function takes i as an input


def AnimationFunction(i):
    y = np.sin(10 * np.pi * (x - 0.01 * i))
    line_plotted.set_data((x, y))


# Used From: matplotlib.animation import FuncAnimation
anim_created = FuncAnimation(fig, AnimationFunction, frames=100, interval=25)
ax3.text(0, -9, "DAEMON", bbox=dict(fill=True, edgecolor='black',
                                    facecolor="white", linewidth=2), fontweight="bold", fontsize=10, size=100)

anim_created.save("../resources/anim.gif", fps=30)
# fig.savefig('anim.jpeg')
# For running in Colab uncomment this lines
# video = anim_created.to_html5_video()
# html = display.HTML(video)
# display.display(html)
plt.close()
