# Tenemos una lista homogénea, luego pedimos al usuario una letra a eliminar, aplicando métodos eliminamos la letra sin importar si esta en mayúscula o minuscula.temp
 

lista = ["A", "B", "b", "c", "E", "E", "f"]
eleccion = input("¿Que letra desea eliminar? ")
eleccion = eleccion.upper()
indice = len(lista)

for temp in lista:
    indice = indice - len(temp)
    if temp.upper() == eleccion:
        continue
    if indice == 0:
        print(temp, end="")
        continue
    print(temp, end=", ")

# EXPLICACIÓN: 
"""Convertimos la elección del usuario en mayúsculas a usando el método .upper()
Creamos una variable y donde guardamos el total de indices de la lista usando el método len() 
Creamos un ciclo for ejecutado en los elementos de la lista y damos las instruciones para imprimir la lista resultante correctamente.
Usamos la sentencia condicional continue para saltar o cambiar las instruciones del ciclo."""