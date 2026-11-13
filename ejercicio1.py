
chefs_registrar = 0
chef_maestro = 0
chef_aprendiz = 0

while chefs_registrar <= 0:
    try:
        chefs_registrar = int(input("Ingrese la cantidad de chefs a registrar: "))
        if chefs_registrar <= 0:
            print ("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")      
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")

for cantidad_chefs in range(chefs_registrar):
    validador_chefs = False
    validador_experiencia = False
    
    while validador_chefs == False:
        codigo_chef = input (f"Ingrese el código del chef {cantidad_chefs+1}: ")
        if len (codigo_chef) < 6 or " " in codigo_chef :
            print ("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        else:
            validador_chefs = True

    while validador_experiencia == False:
        try:
            experiencia_chef = int(input (f"Ingrese la experiencia del chef {cantidad_chefs+1} (en años): "))
            if experiencia_chef <= 0:
                print ("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
            else:
                validador_experiencia = True  
        except:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")

    if experiencia_chef > 8:
        chef_maestro += 1
    else:
        if experiencia_chef <= 8:
            chef_aprendiz += 1

print (f"¡La escuela cuenta con {chef_maestro} Chefs Maestros y {chef_aprendiz} Chefs Aprendices! ¡A cocinar!")
