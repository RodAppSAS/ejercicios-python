filas = int(input("¿Cuantas filas tendrá la matrix? "))
columnas = int(input("¿Cuantas columnas tendrá la matrix? "))

matrix = []

for i in range (filas):
    actual = []
    for _ in range(columnas):
        actual.append(int(input(f"Introduce un valor a {i}: ")))
  
    matrix.append(actual)

for temp in matrix:
    print(temp)

