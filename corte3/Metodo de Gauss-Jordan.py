# Método de Gauss-Jordan Solución a Sistemas de Ecuaciones de la forma A.X=B
import numpy as np
#Ingredo de los datos
A = np.array([[3,2,3],
              [1,5,7],
              [5,6,8]])

B = np.array([[60.70],
              [92.90],
              [56.30]])

#Procedimientos 
casicero = 1e-15 # Considerar como 0

# Evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

# Matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

# Pivoteo parcial por filas
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[dondemax+i,:]
        AB[dondemax+i,:] = temporal       
AB1 = np.copy(AB)

# eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = AB[i,i]
    ade = i + 1
    for k in range(ade,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

# elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    # diagonal a unos
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcolumna])
X = np.transpose([X])

print('Resultado Matriz aumentada:')
print(AB0)
print('Resultado Pivoteo parcial por filas')
print(AB1)
print('Resultado Eliminacion hacia adelante')
print(AB2)
print('Resultado Eliminación hacia atrás')
print(AB)
print('Resultado solución de X: ')
print(X)