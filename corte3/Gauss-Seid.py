import numpy as np

# from read import readMatrix

def readMatrix(path="matrix.dat"):

    file = open(f"{path}", "r")

    #  Read the file and convert it to a list
    data = file.read()
    data = data.split("\n")

    rows = 0
    columns = 0
    

    for line in data:

        if 'rows' in line:
            rows = int(line.split(":")[1])
        if 'columns' in line:
            columns = int(line.split(":")[1])

    print(f"Rows: {rows}\nColumns: {columns}")

    matrix = np.zeros((rows,columns)) # Matrix
    arrayb = np.zeros((columns))  # Array b

    take_matrix_data = False
    take_arrayb_data = False

    i = 0
    for line in data:

        if '# End' in line:
            i = 0
            take_matrix_data = False
            take_arrayb_data = False
        

        if take_matrix_data:
            row = line.split(" ")
            matrix[i] = np.array([float(i) for i in row])

            i += 1
        
        if take_arrayb_data:
            arrayb[i] = float(line)
            i += 1

        if '# name: A' in line:
            take_matrix_data = True

        if '# name: b' in line:
            take_arrayb_data = True

    
    return matrix, arrayb


# Obtener los valores de a matriz
matriz, vector = readMatrix()
rows = np.shape(matriz)[0]
columns = np.shape(matriz)[1]

print("Matriz Leida")
print(f"{matriz}\n")

#Vector solucion
vector_solution=np.zeros(rows)

tolera = 0.000001
iteraciones=50

diferencia = np.ones(rows, dtype=float)
error = 2*tolera

count = 0
while not(error<=tolera or count>iteraciones):
    print(f"Iteración: {count}")
    # por fila
    for i in range(rows):
        # por columna
        suma = 0 
        for j in range(columns):
            # excepto diagonal de A
            if (i!=j): 
                suma = suma-matriz[i,j]*vector_solution[j]
        
        nuevo = (vector[i]+suma)/matriz[i,i]
        diferencia[i] = np.abs(nuevo-vector_solution[i])
        vector_solution[i] = nuevo
    error = np.max(diferencia)
    count += 1


# Respuesta X en columna
vector_solution = np.transpose([vector_solution])
converge = count > iteraciones

# rComprobar que Ax y b son iguales o aproximados
verifica = np.array([ float("{:.3f}".format(value[0]))  for value in np.dot(matriz, vector_solution)])

# SALIDA
print('\nSolución: ')
for i in range(columns):
    print(f"x{i} : {vector_solution[i][0]}")

print(f"\nAx : {verifica}\nb  : {vector}")


# revisa si NO converge
if (converge):
    print("\n\t|LA SOLUCIÓN CONVERGE|\n")