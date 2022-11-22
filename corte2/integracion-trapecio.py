import numpy as np
import matplotlib.pyplot as plt

fx=lambda x: np.sqrt(x)*np.sin(x)
a=1
b=3
tramos=128

muestras=tramos+1
h=(b-a)/tramos
suma_total=0
xi=a
for i in range(0,tramos,1):
    atrapecio=h*(fx(xi)+fx(xi+h))/2
    suma_total=suma_total+atrapecio
    xi=xi+h
integral=suma_total

xi=np.linspace(a,b,muestras)
fi=fx(xi)

muestralinea=muestras*10
xk=np.linspace(a,b,muestralinea)
fk=fx(xk)

print('tramos: ',tramos)
print('integral: ',integral)

plt.plot(xi,fi,'ro')
plt.plot(xk,fk)

plt.fill_between(xi,0,fi,color='g')
for i in range(0,muestras,1):
    plt.axvline(xi[i],color='w')
plt.show()


