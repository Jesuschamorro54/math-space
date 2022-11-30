import numpy as np

# from read import readMatrix

# Esta función es para leer el archivo .dat (puede ser un bloc de notas) y devolver la matriz
def readMatrix(path="C:\dev\Cursos\Metodos numericos\corte3\matrix2.dat"):

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

matriz, vector = readMatrix()  # Atrapo la matriz

rows = np.shape(matriz)[0]  # obtendo el numero de filas
columns = np.shape(matriz)[1]  # obtendo el numero de columnas

print("Matriz Leida: ")
print(f"{matriz}\n")  # Imprimo la matriz que leí

#Vector solucion
vector_solution=np.zeros(rows) # Creo un vector con ceros de tamaño de filas

tolera = 0.00000001
iteraciones=50  # NUmero de iteraciones maximas en caso de no alcanzar la tolerancia

diferencia = np.ones(rows, dtype=float)  # Creo un vector con unos
error = 2*tolera

count = 0
while not(error<=tolera or count>iteraciones):

    print(f"Iteración: {count}")  # Imprimo por las iteraciones
    
    # por fila
    for i in range(rows):
        
        suma = 0
        
        # por columna
        for j in range(columns):
            # Recorro toda la matriz excepto su diagonal para realizar las operaciones se deben hacer (Metodo de Seid)
            if (i!=j): 
                suma = suma-matriz[i,j]*vector_solution[j]
        
        # Realizo las operaciones necesarias lo guardo en nuevo y luego lo meto en vector_solución
        # Este vector solución cambia su valor por cada iteración hasta que termine con todas las iteraciones o llegue a la tolerancia
        nuevo = (vector[i]+suma)/matriz[i,i]
        diferencia[i] = np.abs(nuevo-vector_solution[i])
        vector_solution[i] = nuevo

    error = np.max(diferencia)  # Verifico el error
    count += 1


# Respuesta X en columna
vector_solution = np.transpose([vector_solution])
converge = count > iteraciones

# Comprobar con np.dot que Ax y b son iguales o aproximados y en seguida lo guardo en un array con np.array
verifica = np.array([ float("{:.3f}".format(value[0]))  for value in np.dot(matriz, vector_solution)])

# SALIDA
print('\nSolución: ')
for i in range(columns):
    print(f"x{i} : {vector_solution[i][0]}")

print(f"\nAx : {verifica}\nb  : {vector}")


# revisa si NO converge
if (converge):
    print("\n\t|LA SOLUCIÓN CONVERGE|\n")