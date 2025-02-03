from productos.product import Producto
class Categoria:
    def __init__(self,codigo,name,products:list=[]):
        self.codigo=codigo
        self.name=name
        self.products=products
    
    def agregarProducto(self,producto:Producto):
        self.products.append(producto)
    def showProdcutsFromCategoria(self):
        if len(self.products)>0:
            for i in self.products:
                print(i)
        else:
            print("La lista de productos esta vacia ,agregue una porfavor opcion 2")