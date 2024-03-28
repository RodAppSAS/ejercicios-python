tup_1 = (1, 2, 3, 4, 5)
tup_2 = (8, 6, 4, 2, 0)

suma = []
for i, _ in zip(tup_1, tup_2):
    suma.append(i + _)
print(f"Tupla 1:       {tup_1}")
print(f"               +")
print(f"Tupla 2:       {tup_2}")
print(f"               ===============")
print(f"Suma:          {tuple(suma)}")