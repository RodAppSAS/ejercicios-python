matriz1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matriz2 = [[9,8,7],
           [6,5,4],
           [3,2,1]]

matriz3 = []

for i in range(len(matriz1)):
    temp = []
    for _ in range(len(matriz1[1])):
        temp.append(matriz1[i][_] + matriz2[i][_]) 
    matriz3.append(temp)

for i in range(len(matriz1)):
    if i == 1:
        print(f"{matriz1[i]} + {matriz2[i]} = {matriz3[i]}")
    else:
        print(f"{matriz1[i]}   {matriz2[i]}   {matriz3[i]}")
