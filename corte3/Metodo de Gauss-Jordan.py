# Método de Gauss-Jordan Solución a Sistemas de Ecuaciones de la forma A.X=B
import numpy as np
#Ingredo de los datos

def checkMatriz(matriz):

    rows = np.shape(matriz)[0]
    columns = np.shape(matriz)[1]

    for i in range(rows):
        for j in range(columns-1):
            if i!=j and matriz[i][j] != 0:
                return False 

    return True

A = np.array([[2, 5, -0],
              [1, 2, -1],
              [-3, -4, 7]])

b_array = np.array([[9],[3],[1]])

# Evitar truncamiento en operaciones
A = np.array(A, dtype=float) 

casicero = 1e-15 # Considerar como 0

# Matriz aumentada
AB = np.concatenate((A,b_array),axis=1)
M_aumentada = np.copy(AB)

# Pivoteo parcial por filas
size = np.shape(AB)
rows = size[0]
columns = size[1]

# Para cada fila en AB
for i in range(rows):
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
for i in range(rows):
    pivote = AB[i,i]
    ade = i + 1
    for k in range(ade, rows):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

# elimina hacia atras
ultfila = rows-1
ultcolumna = columns-1
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
print(M_aumentada)
print('Resultado Pivoteo parcial por filas')
print(AB1)
print('Resultado Eliminacion hacia adelante')
print(AB2)
print('Resultado Eliminación hacia atrás')
print(AB)
print('Resultado solución de X: ')
print(X)
print("ESTADO: ", checkMatriz(AB))