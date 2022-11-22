import numpy as np
import sympy as sym

xi=np.array([0,0.2,0.3,0.4])
fi=np.array([1,1.6,1.7,2.0])

#procedimiento
n=len(xi)
x=sym.Symbol('x')
polinomio=0

for i in range(0,n,1):
    numerador=1
    denominador=1
    
    for j in range (0,n,1):
    
        if (i!=j):
    
            numerador=numerador*(x-xi[j])
    
            denominador= denominador *(xi[i]-xi[j])
        
        termino=(numerador/denominador)*fi[i]
    
    polinomio=polinomio+termino

polisimple=sym.expand(polinomio)
px=sym.lambdify(x,polinomio)
#vectores para graficas
muestras=51
a=np.min(xi)
b=np.max(xi)
p_xi=np.linspace(a,b,muestras)
pfi=px(p_xi)

print("polinomio")
print(polinomio)
print("polisimple")
print(polisimple)

