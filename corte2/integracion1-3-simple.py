import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)*np.sin(x)
x=np.linspace(0,np.pi,101)
plt.plot(x,f(x))
plt.grid()
plt.show()

def simpson13(f,a,b):
    m=(a+b)/2
    integral=(b-a)/6*(f(a)+4*f(m)+f(b))
    return(integral)
a=0
b=np.pi
n=40
h=(b-a)/n
suma_total=0
for i in range(n):
    b=a+h
    area=simpson13(f,a,b)
    suma_total=suma_total + area
    a=b
print (suma_total)  
vt=np.exp(np.pi)/2+1/2
errorporcent=abs((vt-suma_total)/vt )*100
print("error %",errorporcent)