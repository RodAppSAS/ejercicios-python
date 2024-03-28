dates = (("Daniel", 23), ("Luis", 21), ("Norida", 29), ("Jhon", 27))
print(dates, "\n")

dates = list(dates)

for i in range(len(dates)):
    for j in range(i + 1, len(dates)):
        if dates[i][1] > dates[j][1]:
            aux = dates[i]
            dates[i], dates[j] = dates[j], aux

print(f"el usuario con menor edad es: {dates[0]}")
print(f"La persona con mayor edad es: {dates[-1]}")