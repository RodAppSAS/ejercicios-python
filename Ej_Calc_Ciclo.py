#Auto reto: Hacer una calculadora usando un ciclo y una sola variable.

"""El programa sólo terminará la ejecución sí el usuario lo decide o selecciona una opción inválida..."""

print("\nCALCULADORA")

print("\n1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

selecc = int(input("\nIngrese una opción o marque '0' para salir: "))

while selecc >= 1 and selecc <= 4:
    if selecc == 1:
        print("\nVamos a sumar")
        selecc = int(input("Dame el primer valor "))
        selecc += int(input("Dame el segundo valor "))
        print("El resultado de la suma es ", selecc)
        selecc = int(input("\nIngrese una opción o marque '0' para salir: "))
        
    elif selecc == 2:
        print("\nVamos a restar")
        selecc = int(input("Dame el primer valor "))
        selecc -= int(input("Dame el segundo valor "))
        print("El resultado de la resta es ", selecc)
        selecc = int(input("\nIngrese una opción o marque '0' para salir: "))

    elif selecc == 3:
        print("\nVamos a multiplicar")
        selecc = int(input("Dame el primer valor "))
        selecc *= int(input("Dame el segundo valor "))
        print("El resultado de la multiplicación es ", selecc)
        selecc = int(input("\nIngrese una opción o marque '0' para salir: "))

    elif selecc == 4:
        print("\nVamos a dividir")
        selecc = int(input("Dame el primer valor "))
        selecc /= int(input("Dame el segundo valor "))
        print("El resultado de la división es ", selecc)
        selecc = int(input("\nIngrese una opción o marque '0' para salir: "))

if selecc == 0:
    print ("\nGracias por usar nuestra App...\n")
else:
    print ("\nOpción inválida...\nGracias por usar nuestra App...\n")