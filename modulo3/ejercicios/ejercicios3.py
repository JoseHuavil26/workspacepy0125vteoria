# estructura para capturar cualquier error 

try:
    #print(0/0)
    lista=[1,2,3,4]
    print(lista[100])
    #tupla=(1,2,23,3,4)
    #tupla[1]=4
except Exception as mesagge:
    print("Error:",mesagge)
