from productos.product import *

class Client:
    def __init__(self,dni,correo,fullname):
        self.dni=dni
        self.correo=correo
        self.fullname=fullname  
        self.carrito_compra=[]
    def activo(self):
        self.activo=True
    def desactivar(self):
        self.activo=False
    def crearPedido(self,pr1:Producto):
        if pr1.hasStock():
            self.carrito_compra.append(pr1)
        else:
            print(f"el producto {pr1.name} no cuenta con stock")