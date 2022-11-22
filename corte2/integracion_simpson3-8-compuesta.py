import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x)*np.sin(x)
def simpson38(f,a,b):
    n1=(2*a+b)/3
    n2=(a+2+b)/3
    integral=(b-a)/8*(f(a)+3*f(n1)+3*f(n2)+f(b))
    return integral

a=0
b=np.pi
n=1
h=(b-a)/(n)
suma_total=0
for i in range(n):
    b=a+h
    area=simpson38(f,a,b)
    suma_total=suma_total + area
    a=b
print (suma_total)  
vt=np.exp(np.pi)/2+1/2
errorporcent=abs((vt-suma_total)/vt )*100
print("error %",errorporcent)