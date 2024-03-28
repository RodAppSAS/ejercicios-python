frase = input("Ingresa una frase: ")
letra = input("¿Con qué letra desea terminar el bucle? ")

for temporal in frase:
    if temporal.lower() == letra.lower():
         break
    elif temporal.lower() == "a" :
        continue
    elif temporal.lower()== "e" :
        continue
    elif temporal.lower() == "i" :
        continue
    elif temporal.lower() == "o" :
        continue
    elif temporal.lower() == "u" :
        continue
    print(temporal, end="_")