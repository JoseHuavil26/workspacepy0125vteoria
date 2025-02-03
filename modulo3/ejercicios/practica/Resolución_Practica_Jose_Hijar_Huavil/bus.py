class Bus:
    def __init__(self, numero):
        self.numero = numero
        self.ruta = ""
        self.horarios = []
        self.conductores = []

    def agregar_horario(self, inicio, fin):
        if inicio < 0 or fin < 0 or inicio >= fin or fin > 24:
            print("Error: El horario debe estar en el rango 0-24 horas y el inicio debe ser menor que el fin.")
            return False

        for existente in self.horarios:
            if not (fin <= existente[0] or inicio >= existente[1]):
                print(f"Error: El horario {inicio}-{fin} se superpone con otro horario {existente[0]}-{existente[1]} en el bus {self.numero}.")
                return False

        self.horarios.append((inicio, fin))
        print(f"Horario: {inicio}-{fin} horas, agregado al bus {self.numero}.")
        return True