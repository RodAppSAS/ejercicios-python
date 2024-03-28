frase = input("Ingresa una frase: ")
frase = frase.replace(" ", "")

dicc = {}
for key in frase:
    if not key in dicc:
        dicc.update({key: 1}) 
    else: 
        dicc [key] += 1

print(dicc)