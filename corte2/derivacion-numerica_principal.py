import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**3+2*x**2+5*x+1

num = 11
a = -2
b = 2

x = np.linspace(a, b, num)
dx = (b-a)/(num-1)

y = f(x)

yp = np.zeros_like(x)
ypp = np.zeros_like(x)
for i in range(num):
    if i == 0:
        yp[i] = (y[i+1] - y[i])/dx
    elif i == num-1:
        yp[i] = (y[i] - y[i-1])/dx
    else:
        yp[i] = (y[i+1] - y[i-1])/(2*dx)

def fp(x):
    return 9*x**2+4*x+5

def fpp(x):
    return 18*x+4

for i in range(num):
    if i == 0:
        ypp[i] = (y[i+2] -2*y[i+1]+y[i])/dx**2
    elif i == num-1:
        ypp[i] = (y[i]-2*y[i-1]+y[i-2])/dx**2
    else:
        ypp[i] = (y[i+1]-2*y[i]+y[i-1])/dx**2

print(yp)

plt.plot(x,fp(x),'g-')
plt.plot(x, yp, 'bo')
plt.show()

plt.plot(x,fpp(x),'g-')
plt.plot(x, ypp, 'bo')
plt.show()
