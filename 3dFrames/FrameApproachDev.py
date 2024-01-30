import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import sin, cos, pi, outer, ones, size, linspace


# Define x, y, z lists for sphere
a = linspace(0, 2 * pi)
b = linspace(0, pi)
x = 10 * outer(cos(a), sin(b))
y = 10 * outer(sin(a), sin(b))
z = 10 * outer(ones(size(a)), cos(b))

# The amount of frames in the animation
frames = 26

# Generate each frame
for n in range(frames):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color=('b'))
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlim(-8,8)
    ax.set_xlim(-8,8)
    ax.set_xlim(-8,8)
    plt.savefig(f"{n}.png")
    plt.close()
    
    # Add 1 to the x so the sphere moves right by 1
    x += 1

# Use pillow to save all frames as an animation in a gif file
from PIL import Image

images = [Image.open(f"{n}.png") for n in range(frames)]

images[0].save('ball.gif', save_all=True, append_images=images[1:], duration=100, loop=0)