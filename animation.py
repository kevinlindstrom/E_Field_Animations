try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk  # Python 2

import numpy as np
from itertools import cycle
from matplotlib import pyplot as plt


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs.pop("end") - kwargs["start"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle_arc = _create_circle_arc

def plotFields():
    # Plotting after simulation (requires one full execution)
    print("Total E Field")
    print(f"In x: {round(np.sum(np.array(dEx_list)),1)} N/C")
    print(f"In y: {round(np.sum(np.array(dEy_list)), 1)} N/C")

    # plt.rcParams['text.usetex'] = True
    plt.rcParams["figure.figsize"] = [8, 5]
    plt.rcParams["figure.autolayout"] = True
    ax1 = plt.subplot(211)
    ax1.grid()
    ax1.title.set_text('Field in $x$ Direction at P')
    ax1.set_xlabel("Distance $x$ Along the Charged Rod (px)")
    ax1.set_ylabel("$dE_x$ Field (N/C)")
    plt.plot(xVal-w/2, dEx_list)
    ax2 = plt.subplot(212)
    ax2.grid()
    ax2.title.set_text('Field in $y$ Direction at P')
    ax2.set_xlabel("Distance $x$ Along the Charged Rod (px)")
    ax2.set_ylabel("$dE_y$ Field (N/C)")
    plt.plot(xVal-w/2, dEy_list)
    plt.show()

def show_xy_dE():
    global show_dEx_dEy
    show_dEx_dEy = not show_dEx_dEy

def changeP():
    global p
    global change_P
    global dEx_list 
    global dEy_list
    change_P = not change_P
    if change_P:
        p = [3*w/4, h/2.5]
    else:
        p = [w/2, h/2.5]
    dEy_list = []
    dEx_list = []


# Draw and run the simulation
def makeAll():
    x = next(list)
    my_canvas.delete('all')
    
    # axes
    my_canvas.create_line(w/2, 0, w/2, h, width=thickness, arrowshape=arrow_tuple, fill="black", arrow=tk.FIRST)
    my_canvas.create_text(w/2+20, 20, text="y", fill="black", font=('Roman 16 italic'))
    my_canvas.create_line(0, h - h/10, w, h - h/10, width=thickness, arrowshape=arrow_tuple, fill="black", arrow=tk.LAST)
    my_canvas.create_text(w-20, 9*h/10+20, text="x", fill="black", font=('Roman 16 italic'))

    # Line charge
    my_canvas.create_rectangle(w/10, h - h/10 + thickness, 9*w/10, h - h/10 - thickness, fill="cyan")
    my_canvas.create_text(w/10, 9*h/10 - 25, text="-l", fill="black", font=('Script 20 italic'))
    my_canvas.create_text(9*w/10, 9*h/10 - 25, text="+l", fill="black", font=('Script 20 italic'))

    # P
    my_canvas.create_circle(p[0], p[1], 6*thickness/4, fill="white")

    # R, dq, dE
    d = 9*h/10 - h/2.5
    x_0 = x-p[0]
    dEx = -(s*x_0)/((x_0**2 + d**2)**(3/2))
    dEy = -(s*d)/((x_0**2 + d**2)**(3/2))

    if len(dEx_list) < len(xVal):
        if len(dEx_list) == 0:
            if x == min(xVal):
                dEx_list.append(dEx)
                dEy_list.append(-1*dEy)
        else:
            dEx_list.append(dEx)
            dEy_list.append(-1*dEy)

    my_canvas.create_text(200, 50, text=f"Total E Field in x: {round(np.sum(np.array(dEx_list)),1)} N/C", fill="black", font=('Roman 16 bold'))
    my_canvas.create_text(200, 100, text=f"Total E Field in y: {round(np.sum(np.array(dEy_list)),1)} N/C", fill="black", font=('Roman 16 bold'))

    # dEx & dEy
    if show_dEx_dEy:
        my_canvas.create_line(p[0], p[1], p[0] + dEx, p[1], width=thickness, arrowshape=arrow_tuple, fill="magenta", arrow=tk.LAST)
        my_canvas.create_line(p[0], p[1], p[0], p[1] + dEy, width=thickness, arrowshape=arrow_tuple, fill="magenta", arrow=tk.LAST)

    # dE
    my_canvas.create_line(p[0], p[1], p[0] + dEx, p[1] + dEy, width=thickness, arrowshape=arrow_tuple, fill="orange", arrow=tk.LAST)
    my_canvas.create_text(p[0] + dEx +30, p[1] + dEy+20, text="d", fill="black", font=('Roman 16 italic'))
    my_canvas.create_text(p[0] + dEx +40, p[1] + dEy+20, text="E", fill="black", font=('Roman 16 bold'))


    my_canvas.create_line(p[0], 9*h/10, p[0], p[1], width=thickness, arrowshape=arrow_tuple, fill="red", arrow=tk.LAST) # ry
    my_canvas.create_line(x, 9*h/10, p[0], 9*h/10, width=thickness, arrowshape=arrow_tuple, fill="red", arrow=tk.LAST) #rx

    # r then dq
    my_canvas.create_line(x, 9*h/10, p[0], p[1], width=thickness, arrowshape=arrow_tuple, fill="blue", arrow=tk.LAST)  # r
    my_canvas.create_text(x + 20 + (p[0]-x)/2, p[1] + (9*h/10 - p[1])/2, text="r", fill="black", font=('Roman 16 bold'))
    my_canvas.create_circle(x, 9*h/10, 10, fill="blue")  # dq
    my_canvas.create_text(x, 9*h/10 + 25, text="dq", fill="black", font=('Roman 16 italic'))

    my_canvas.after(delay, makeAll)
        

# Main code
root = tk.Tk()
root.title('Continuous Charge Distribution on a Rod Animation')

w = 1200 #1920/2
h = 800 #1080/2
thickness = 5
arrow_tuple = (8*thickness/2, 10*thickness/2, 3*thickness/2)
s = 5*10**7
show_dEx_dEy = False
change_P = False
p = [w/2, h/2.5]


root.geometry(f"{w+100}x{h+150}")
my_canvas = tk.Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

bottom = tk.Frame(root)
bottom.place(x=w/2-75, y=h+20)
# Create Plotting Button
B1=tk.Button(root,text="Make Plots",command=plotFields)
B1.pack(in_=bottom, side=tk.RIGHT)
B2=tk.Button(root,text="Show dEx & dEy",command=show_xy_dE)
B2.pack(in_=bottom, side=tk.LEFT)
B3=tk.Button(root,text="Change P",command=changeP)
B3.pack(in_=bottom, side=tk.LEFT)

# Points to sweep
xVal = np.arange(w/10, 9*w/10 + 1, 3)
num_x_pts = len(xVal)
list = cycle(xVal)
delay = 20
dEy_list = []
dEx_list = []

my_canvas.after(delay, makeAll)
root.mainloop()
