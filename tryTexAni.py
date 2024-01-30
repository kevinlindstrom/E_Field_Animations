try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # Python 2

import numpy as np

from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs.pop("end") - kwargs["start"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc


# def _create_thick_line(self, x1, y1, x2, y2, thickness=7, fill="black"):
#     my_canvas.create_rectangle(x1 + thickness/2)

#     if "start" in kwargs and "end" in kwargs:
#         kwargs["extent"] = kwargs.pop("end") - kwargs["start"]
#     return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
# tk.Canvas._create_thick_line = _create_thick_line


# Use TkAgg in the backend of tkinter application (for Latex)
matplotlib.use('TkAgg')

root = tk.Tk()
root.title('Contineous Charge Distribution Animation')
root.geometry("1000x700")
w = 1920/2
h = 1080/2
dpi = 100

"""
For Latex
"""
frame = tk.Frame(root)
frame.pack()
# Create an Entry widget
var = tk.StringVar()
entry = tk.Entry(frame, width=70, textvariable=var)
entry.pack()
label = tk.Label(frame)
label.pack()

# Define the figure size and plot the figure
fig = matplotlib.figure.Figure(figsize=(w/dpi, h/dpi), dpi=dpi)
wx = fig.add_subplot(111)
my_canvas = FigureCanvasTkAgg(fig, master=label)
my_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
my_canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Set the visibility of the Canvas figure
wx.get_xaxis().set_visible(False)
wx.get_yaxis().set_visible(False)

"""
Figure
"""
# my_canvas = tk.Canvas(root, width=w, height=h, bg="white")
# my_canvas.pack(pady=20)




# axes
my_canvas.create_line(w/2, 0, w/2, h, width=3, fill="black", arrow=tk.FIRST)
my_canvas.create_line(0, h - h/10, w, h - h/10, width=3, fill="black", arrow=tk.LAST)

# Line charge
# thicknessLC_relative = 10
my_canvas.create_rectangle(w/10, h - h/10 + 5, 9*w/10, h - h/10 - 5, fill="cyan")

# P
p = [w/2, h/2.5]
my_canvas.create_circle(w/2, h/2.5, 6, fill="white")


# Points to sweep
x = np.arange(w/10, 9*w/10 + 1, 5)
# x = np.arange(96,10,1)
# print(x)

# R, dq, dE
n = 100
my_canvas.create_line(x[n], 9*h/10, p[0], p[1], width=3, fill="blue", arrow=tk.LAST)
my_canvas.create_circle(x[n], 9*h/10, 10, fill="blue")
d = 9*h/10 - h/2.5
s = 3*10**7
x_0 = x[n]-w/2
dEx = -(s*x_0)/((x_0**2 + d**2)**(3/2))
dEy = -(s*d)/((x_0**2 + d**2)**(3/2))
my_canvas.create_line(p[0], p[1], p[0] + dEx, p[1] + dEy, width=3, fill="orange", arrow=tk.LAST)
my_canvas.create_line(w/2, 9*h/10, w/2, p[1], width=3, fill="red", arrow=tk.LAST)
my_canvas.create_line(x[n], 9*h/10, w/2, 9*h/10, width=3, fill="red", arrow=tk.LAST)

# Test Latex








root.mainloop()