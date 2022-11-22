import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

def dydx(x,y):
    return y*np.sqrt(x)
n=10
x0=0
xf=2
y0=1
h=(xf-x0)/n

x=[x0]
y=[y0]

for i in range(n):
    y0=y0+h*dydx(x0,y0)
    y.append(y0)
    x0=x0+h
    x.append(x0)
print(y[-1])