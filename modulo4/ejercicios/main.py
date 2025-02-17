from lib.bd import InitBd
from lib.funcionalidad import RegistrarUsuario
bd_conexion=InitBd()

def Menu():
    mensage="""
        1. Registrar nuevo usuario
        2. Registrar nuevo producto
        3. Registrar nuevo provedor
        4. Ver usuarios
        5. ver productos
        6. ver provedores
        7. dar de baja un provedor
        8. Salir
    """
    print(mensage)
    
    
if __name__=="__main__":
    while True:
        Menu()
        opcion=int(input("ingrese una opcion: "))
        match opcion:
            case 1:
                RegistrarUsuario()
                pass
            case 2:
                pass
            case 8:
                break