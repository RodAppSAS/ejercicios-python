primos = []

for i in range(2,100):
    primos.append(i)
    for _ in range(i-1,1,-1): 
       if i % _ == 0:
        primos.remove(i)
        break
print(primos)
