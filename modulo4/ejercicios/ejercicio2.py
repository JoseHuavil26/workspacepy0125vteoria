class Client:
    def __init__(self):
        self.addUser()
    def setRisk(self,risk):
        self.risk=risk
    def addUser(self):
        self.fullname=input("ingrese su fullname: ")
        self.email=input("ingrese su email: ")
        self.salary=int(input("ingrese su salary: "))
        self.dni=input("ingrese su dni: ")
    def setRisk(self):
        risk=float(input('ingrese el risk del cliente'))
        if risk<0.5:
            return 'NO-APROBADO'
        return 'APROBADO'

    def __str__(self):
        return f"ingresa cliente"
    def toString(self):
        risk=self.setRisk()
        return f"{self.fullname},{self.email},{self.dni},{self.salary},{risk}\n"
def RegisterUser():

    ruta="/workspaces/workspacepy0125v2/modulo4/ejercicios/files/user.txt"

    with open(ruta,mode='a') as file:
        c1=Client()
        c1String=c1.toString()
        file.write(c1String)
        file.close()
RegisterUser()

