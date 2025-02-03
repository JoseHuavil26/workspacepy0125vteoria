from bus import Bus
from conductor import Conductor

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self):
        numero = input("Ingrese el número del bus: ")
        bus = Bus(numero)
        self.buses.append(bus)
        print(f"Bus {numero} agregado.")
    
    def agregar_ruta_bus(self):
        numero = input("Ingrese el número del bus: ")
        ruta = input("Ingrese la ruta del bus: ")
        
        for bus in self.buses:
            if bus.numero == numero:
                bus.ruta = ruta
                print(f"Ruta {ruta} agregada al bus {numero}.")
                return
        print("Bus no encontrado.")
    
    def registrar_horario_bus(self):
        numero = input("Ingrese el número del bus: ")
        inicio = int(input("Ingrese la hora de inicio: "))
        fin = int(input("Ingrese la hora de fin: "))
        
        for bus in self.buses:
            if bus.numero == numero:
                bus.agregar_horario(inicio, fin)
                return
        print("Bus no encontrado.")
    
    def agregar_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado.")
    
    def agregar_horario_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        inicio = int(input("Ingrese la hora de inicio del conductor: "))
        fin = int(input("Ingrese la hora de fin del conductor: "))
        
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                conductor.agregar_horario(inicio, fin)
                return
        print("Conductor no encontrado.")
    
    def asignar_bus_conductor(self):
        numero_bus = input("Ingrese el número del bus: ")
        nombre_conductor = input("Ingrese el nombre del conductor: ")

        bus = None
        conductor = None
        for b in self.buses:
            if b.numero == numero_bus:
                bus = b
                break
        for c in self.conductores:
            if c.nombre == nombre_conductor:
                conductor = c
                break

        if bus and conductor:
            if conductor.horarios == []:
                print(f"No hay horarios asignados al conductor {nombre_conductor}.")
            else:
                bus.conductores.append(conductor)
                conductor.buses.append(bus)
                print(f"Conductor {nombre_conductor} asignado al bus {numero_bus}.")
        else:
            print("Bus o conductor no encontrado.")

    
    def mostrar_informacion(self):
        print("\n----- Información de Buses -----")
        for bus in self.buses:
            print(f"\nBus {bus.numero} - Ruta: {bus.ruta}, Horarios: {bus.horarios}")
            
            if bus.conductores:
                print("Conductores asignados:")
                for conductor in bus.conductores:
                    print(f"- {conductor.nombre} | Horarios: {conductor.horarios}")
            else:
                print("No hay conductores asignados.")

        print("\n----- Información de Conductores -----")
        for conductor in self.conductores:
            print(f"\nConductor {conductor.nombre} - Horarios: {conductor.horarios}")
            
            if conductor.buses:
                print("Buses asignados:")
                for bus in conductor.buses:
                    print(f"- Bus {bus.numero} | Ruta: {bus.ruta} | Horarios: {bus.horarios}")
            else:
                print("No hay buses asignados.")