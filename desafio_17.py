names = ("Daniel", "Fernando", "Norida", "Jhon", "Rudy", "German")
print(names)

num = int(input(f"\nIntruduce un numero entero entre 0 y {len(names) - 1}: "))

while num < 0 or num > len(names) - 1:
    print("¡Error!: Número inválido, vuelve a intentar.")
    num = int(input(f"\nIntruduce un numero entero entre 0 y {len(names) - 1}: "))

print(f"El nombre es: {names[num]}")