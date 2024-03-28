#Permiten poner varias condiciones, en caso de que la primera no se cumpla se ejecuta la segunda y asi sucesivamente.

"""Si no se cumple la condicional 'if' se pueden agregar varias condicionales 'elif'.
Si no se cumple ni la condicional 'if' ni las condicional 'elif' seria un 'else'.
"""


print("PROGRAMA PARA SABER CUAL NUMERO ES MAS GRANDE\n")

valor1 = int(input("Ingresa el primer numero: "))
valor2 = int(input("Ingresa el segundo numero: "))
valor3 = int(input("Ingresa el tercer numero: "))

if valor1 > valor2 and valor1 > valor3 :
    print("\nEl número ", valor1, " es el mas grande.")

elif valor2 > valor3:
    print("\nEl número ", valor2, " es el mas grande.")

else:
    print("\nEl número ", valor3, " es el mas grande.")