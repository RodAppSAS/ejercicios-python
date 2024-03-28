tabla = int(input("¿Que tabla de multiplicar deseas ver? "))
while tabla >= 1:
    print(f"\nLa tabla del {tabla} es: ")
    for temp in range(1,11) :
         print(f"{tabla} X {temp} = {tabla * temp}" )
    tabla = int(input("\n¿Que otra tabla desea consultar? O marca '0' para salir: "))
print("\nGracias por usar nuestra app...\n")