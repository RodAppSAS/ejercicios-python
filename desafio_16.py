numbers = (5, 8, 3, 3, 1, 6, 2)
print(f"Tupla original: {numbers}\n")

selecc = int(input("¿Cuál de estos números quieres modificar por 0? "))
numbers = list(numbers)
len_numbers = len(numbers)

for i in range(len_numbers):
    if numbers[i] == selecc:
        numbers[i] = 0
numbers = tuple(numbers)
    
print(f"\nTupla modificada: {numbers}")