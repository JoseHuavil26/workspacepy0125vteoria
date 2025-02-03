def sumar2(numero):
    return numero+2

def GetNumbers():
    new_numero=None
    try:
        n=int(input("ingrese un numero"))
        new_numero=10/n
    except:
        print("lo de arriba fallo")
        new_numero=0
    else:
        print("funciono corectamente")
    finally:
        print(sumar2(new_numero))

GetNumbers()