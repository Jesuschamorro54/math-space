import numpy as np
import sympy as sym

vector_x=np.array([1,3,5,])
vector_y=np.array([4.75,5.25,19.75])

#procedimiento

xp = sym.Symbol('x')
polinomio = 0

for i in range(len(vector_x)):
    numerador=1
    denominador=1
    
    for j in range (len(vector_x)):
    
        if (i!=j):
    
            numerador *= (xp-vector_x[j])
    
            denominador *= (vector_x[i]-vector_x[j])
        
        termino=(numerador/denominador)*vector_y[i]
    
    polinomio=polinomio+termino

polisimple=sym.expand(polinomio)
px=sym.lambdify(xp,polinomio)


print(polisimple)

