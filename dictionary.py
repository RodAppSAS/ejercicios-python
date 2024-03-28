# Ejercicio #1:
fruits = {"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(f"\nEjercicio #1: \n{fruits}")

p_manzana = fruits.get("manzanas")
print(p_manzana)

# Ejercicio #2:
fruits = {"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(f"\nEjercicio #2: \n{fruits}")

fruits.update({"bananas": 5, "mangos": 6, "uvas": 3})
print(fruits)

# Ejercicio #3:
fruits = {"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(f"\nEjercicio #3: \n{fruits}")
fruits.pop("peras")
print(fruits)

# Ejercicio #4:
fruits = {"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
list_key = []
list_values = []
for key, values in fruits.items():
    list_key.append(key)
    list_values.append(values)

print(f"\nEjercicio #4\nDiccionario: {fruits}\nLista de claves: {list_key}\nLista de valores: {list_values}")

# Ejercicio #5:
fruits = {"manzanas": 5,
        "peras": 2,
        "naranjas": 4
        }
print(f"\nEjercicio #5: \n{fruits}")

if "manzanas" in fruits:
    print(True)
else:
    print(False)