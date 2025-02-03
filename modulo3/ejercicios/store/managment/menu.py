#from productos.action import showProducts
from productos.action import *
from productos.categoria import *
def Menu():
    msg="""
    BIENVENIDO A LA TIENDA
    1.VER PRODUCTOS
    2.AGREGAR PRODUCTO
    3.AGREGAR CATEGORIA
    4.AGREGAR CLIENTE
    5.REALIZAR UN PEDIDO
    6.SALIR
    """ 
    c1=Categoria("TECH","Tecnologia")

    while True:
        print(msg)
        opcion=int(input("ingrese una opcion del menu:"))
        match opcion:
            case 1:
                #showProducts(c1.products)
                c1.showProdcutsFromCategoria()
                pass
            case 2:
                agregarProducto(c1.products)
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("Hasta luego")
                break
            case _:
                print("ingrese una opcion valida")
