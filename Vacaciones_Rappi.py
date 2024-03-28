print("VACACIONES 2023 RAPPI")

nombre = input("\nDame tu nombre: ")
clave = int(input("\nHola " + nombre + ", digita la clave de tu area de trabajo: "))

if clave == 1:
    tiempo = int(input("Cuantos años llevas trabajando? "))
    
    if tiempo == 1:
        print(nombre + ", los trabajadores de Atencion al cliente con ", tiempo, " años de trabajo tienen derecho a 6 dias de vacaciones.")
    if tiempo >= 2 and tiempo <= 6:
        print(nombre + ", los trabajadores de Atencion al cliente con ", tiempo, " años de trabajo tienen derecho a 14 dias de vacaciones.")
    if tiempo > 6:
        print(nombre + ", los trabajadores de Atencion al cliente con ", tiempo, " años de trabajo tienen derecho a 20 dias de vacaciones.")
    if tiempo < 1:
        print ("Aún no tienes derecho a vacaciones.")

if clave == 2:
    tiempo = int(input("Cuantos años llevas trabajando? "))
    
    if tiempo == 1:
        print(nombre + ", los trabajadores de Logística con ", tiempo, " años de trabajo tienen derecho a 7 dias de vacaciones.")
    if tiempo >= 2 and tiempo <= 6:
        print(nombre + ", los trabajadores de Logística con ", tiempo, " años de trabajo tienen derecho a 15 dias de vacaciones.")
    if tiempo > 6:
        print(nombre + ", los trabajadores de Logística con ", tiempo, " años de trabajo tienen derecho a 22 dias de vacaciones.")
    if tiempo < 1:
        print ("Aún no tienes derecho a vacaciones.")

if clave == 3:
    tiempo = int(input("Cuantos años llevas trabajando? "))
    
    if tiempo == 1:
        print(nombre + ", los trabajadores de Gerencia con ", tiempo, " años de trabajo tienen derecho a 10 dias de vacaciones.")
    if tiempo >= 2 and tiempo <= 6:
        print(nombre + ", los trabajadores de Gerencia con ", tiempo, " años de trabajo tienen derecho a 20 dias de vacaciones.")
    if tiempo > 6:
        print(nombre + ", los trabajadores de Gerencia con ", tiempo, " años de trabajo tienen derecho a 30 dias de vacaciones.")
    if tiempo < 1:
        print ("Aún no tienes derecho a vacaciones.")
else:
    print("La clave es incorrecta")

    

        
        

    





    

    
    
