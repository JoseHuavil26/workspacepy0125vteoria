from productos.product import Producto
def showProducts(lista_producto:list):
    if len(lista_producto)>0:
        for i in lista_producto:
            print(i)
    else:
        print("La lista de productos esta vacia ,agregue una porfavor opcion 2")


def agregarProducto(lista:list):
    codigo=input("ingrese el codigo:")
    nombre=input("ingrese el nombre:")
    precio=float(input("ingrese el precio:"))
    stock=int(input("ingrese el stock:"))
    dimensiones=input("ingrese el dimensiones:")
    pr1=Producto(codigo,nombre,precio,stock,dimensiones)
    lista.append(pr1)