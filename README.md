# E_Field_Animations
The `animate.py` file creates a tkinter window that simulates the summation of 
all of the $d\vec{\mathbf{E}}$ fields to highlight how the symmetry of the 
problem causes the net $\vec{\mathbf{E}}$ field to only be in the 
$\pm\hat{\mathbf{y}}$ directions. There are multiple buttons that affect the 
simulation, some changes need the sweep to repeat to go into effect.
The total fields change over the first sweep until they rest at their net values.

Given the choice of the window size, the field in the $\pm\hat{\mathbf{x}}$ directions may not fully go to zero 
if the coordinates swept over are not symmetric about the $y$ axis (I hope to 
fix this shortly).

There are no physical units of charge in this simulation, just a scale variable
`s` that can be used to change the size of $d\vec{\mathbf{E}}$ such that it
neatly fits well on the plot.

## Installation Instructions:
You most likely already have everything you need if you already use python. In 
case you require anything to run `animation.py`, see below

### Python & PIP 
#### Install python + pip on Linux OS with apt:
```
sudo apt install python3
sudo apt install python3-pip
```

#### Windows install:
Install python3:
*  from [Windows Store](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare) (automatically adds python to PATH).

* from [executable](https://www.python.org/downloads/windows/) (must [add python to PATH](https://phoenixnap.com/kb/add-python-to-path))

Get and Install PIP:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
* Be sure to add pip to PATH, [explained here](https://phoenixnap.com/kb/install-pip-windows).

### Install required packages

One pip is installed: `numpy`, `tkinter`, and `matplotlib` are all required to run the code

```
pip3 install numpy
pip3 install tk
pip3 install matplotlib
```

