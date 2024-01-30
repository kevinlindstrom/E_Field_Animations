import tkinter as tk
from itertools import cycle

RADIUS = 5
DELAY = 1000  # milliseconds
WIDTH, HEIGHT = 500, 500

coordinates = [(100, 50), (200, 200), (300, 250), (400, 300)]

def move():
    x, y = next(cycled_coordinates)
    canvas.coords(dot, x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS)
    canvas.after(DELAY, move)

cycled_coordinates = cycle(coordinates)

master = tk.Tk()

canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT)
canvas.pack()

x, y = next(cycled_coordinates)

dot = canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, fill='red')

canvas.after(DELAY, move)

master.mainloop()