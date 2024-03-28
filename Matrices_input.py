preg = int(input("¿Cuántas matrices vamos a sumar? "))

while preg <= 1:
    print("Se necesitan dos o mas matrices para realizar la suma...")
    preg = int(input("¿Cuántas matrices vamos a sumar? "))

num_f = int(input("¿Cuántas filas tendran las matrices: "))
num_c = int(input("¿Cuántas columnas tendran las matrices: "))

#Llenado de matrices:
matrices = []
for mat in range(preg):
    matrix =[]
    for i in range(num_f):
        fila = []
        for col in range(num_c):
            fila.append(int(input(f"Ingrese el valor de la matrix {mat+1} fila {i} columna {col}: ")))
        matrix.append(fila)
    matrices.append(matrix)

# Suma de matrices:
matrix = []
for i in range(num_f):
    filas =[]
    for col in range(num_c):
        suma = 0
        for mat in range(len(matrices)):
            suma += matrices[mat][i][col]
        filas.append(suma)
    matrix.append(filas)
matrices.append(matrix)

# Imprimir matrices:
for fila in range(num_f):
    for mat in range(len(matrices)):
        if fila != 1:
            print(f"{matrices[mat][fila]}", end="   ")
        else:
            if mat < len(matrices) -2:
                print(f"{matrices[mat][fila]}", end=" + ")
            elif mat < len(matrices) -1:
                print(f"{matrices[mat][fila]}", end=" = ")
            else:
                print(f"{matrices[mat][fila]}", end="   ")
    print()