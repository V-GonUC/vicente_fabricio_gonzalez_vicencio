camarotes_disponibles = 90
op = 0
reserva_camarotes = 0 
historial_reservas = 0
print ("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

while op != 5:    
        
    print ('=== MENÚ PRINCIPAL ===')
    print ('1. Camarotes disponibles.')
    print ('2. Reservar camarote.')
    print ('3. Cancelar camarote.')
    print ('4. Historial de reservas.')
    print ('5. Salir.')

            
    try:
            op = int(input('Ingrese una opción: '))
    except:
            op = 0
            
    if op < 1 or op > 5:
            print("¡Error de opción! Ingresa un número entero positivo del 1 al 5 para continuar.")
    
    match op:
            case 1:
                print(f"La cantidad de camarotes disponibles es: {camarotes_disponibles}")
        
            case 2:
                reserva_valida = False
                while reserva_valida == False:
                    try:
                        if camarotes_disponibles == 0:
                            print("Error: No hay camarotes disponibles para reservar, libere camarotes antes de reservar más.")
                            reserva_valida = True
                            continue
                        
                        reserva_camarotes = int(input("Ingrese la cantidad de camarotes que desea reservar: "))
                        if reserva_camarotes <=0:
                            print("¡Error de reserva! Ingresa un número entero positivo para reservar camarotes.")
                        elif reserva_camarotes > camarotes_disponibles:
                            print("¡Error de reserva! No hay suficientes camarotes disponibles para reservar.")
                            reserva_valida = True
                        else:
                            camarotes_disponibles -= reserva_camarotes
                            historial_reservas += 1
                            print(f"¡Reserva exitosa!")
                            reserva_valida = True

                    except:
                            print("¡Error de reserva! Ingresa un número entero positivo para reservar camarotes.")
            
            case 3:
                try:
                    liberar_camarotes = int(input("Ingrese la cantidad de camarotes que desea liberar: "))
                    if liberar_camarotes <= 0:
                        print("¡Error de cancelación! Ingresa un número entero positivo para liberar camarotes.")
                    elif liberar_camarotes > 90 - camarotes_disponibles:
                        print("¡Error de cancelación! No hay suficientes camarotes reservados para liberar.")       
                    else:
                        camarotes_disponibles += liberar_camarotes
                        historial_reservas -= 1
                        print(f"¡Cancelación exitosa!")
                except:
                    print("¡Error de cancelación! Ingresa un número entero positivo para liberar camarotes.")
            
            case 4:
                print (f"El historial de reservas es: {historial_reservas}")
            
            case 5: print ("Gracias por utilizar nuestro software, hasta la próxima.")

    