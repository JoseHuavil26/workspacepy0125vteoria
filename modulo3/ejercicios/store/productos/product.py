""" def Product():
    lista_producto=["product3","product3","product2"]
    return lista_producto

def showProducts():
    lista=Product()
    for i in lista:
        print(i)
 """

class Producto:
    def __init__(self,codigo,nombre,precio,stock,dimensiones):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.dimensiones=dimensiones
    
    def setPerecible(self,fecha_caducidad):
        self.isPerecible=True
        self.fecha_caducidad=fecha_caducidad
    def setPromocion(self,descuento:float):
        self.promocion=True
        self.descuento=100-descuento
    def precioFinal(self):
        # multiplicarlo x100 y divirlo => 1.50 => 150/34
        if self.promocion:
            return self.precio(self.descuento)/100
        return self.precio
    def disabledPromocion(self):
        self.promocion=False
    def getSizes(self):
        dimensiones=self.dimensiones.spli("*")
        try:
            self.sizes={
                "altura":dimensiones[0],
                "largo":dimensiones[1],
                "ancho":dimensiones[2]
            }
        except:
            print("error no tiene 3 dimensiones")
            self.dimension=input("ingrese dimension correcta:")
    def hasStock(self):
        return self.stock>0
    def __str__(self):
        if hasattr(self, "promocion"):
            return f"#PROMOCION #El producto de codigo {self.codigo} de nombre {self.nombre} tiene un stock {self.stock}"    
        return f"El producto de codigo {self.codigo} de nombre {self.nombre} tiene un stock {self.stock}"


