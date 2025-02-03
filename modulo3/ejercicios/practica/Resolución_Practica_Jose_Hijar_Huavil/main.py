from admin import Admin

def menu():
    admin = Admin()
    
    while True:
        print("\n----- MENÚ GESTIÓN DE TICKETS -----")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Agregar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Mostrar información agregada")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                admin.agregar_bus()
            case "2":
                admin.agregar_ruta_bus()
            case "3":
                admin.registrar_horario_bus()
            case "4":
                admin.agregar_conductor()
            case "5":
                admin.agregar_horario_conductor()
            case "6":
                admin.asignar_bus_conductor()
            case "7":
                admin.mostrar_informacion()
            case "8":
                print("Saliendo del programa.¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu()