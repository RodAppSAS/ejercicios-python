
# Tengo una lista de 5 elementos tipo int y debo eliminar el primero y el ultimo elemento.

"""Debo imprimir la lista original, la lista resultante y una lista con los elementos eliminados..."""


lista = [1, 2, 3, 4, 5]
print(f"Lista números {lista}")

elim = []

for i in lista:
    if i == 1 or i == 5:
        lista.remove(i)
        elim.append(i)
print(f"Lista números: {lista}\nLista números eliminados: {elim}")