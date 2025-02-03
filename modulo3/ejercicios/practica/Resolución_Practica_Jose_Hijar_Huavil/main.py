from admin import Admin

def menu():
    admin = Admin()
    
    while True:
        print("\n----- MENÚ -----")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Agregar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Mostrar información agregada")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            admin.agregar_bus()
        elif opcion == "2":
            admin.agregar_ruta_bus()
        elif opcion == "3":
            admin.registrar_horario_bus()
        elif opcion == "4":
            admin.agregar_conductor()
        elif opcion == "5":
            admin.agregar_horario_conductor()
        elif opcion == "6":
            admin.asignar_bus_conductor()
        elif opcion == "7":
            admin.mostrar_informacion()
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()