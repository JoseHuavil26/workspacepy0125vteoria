# metodos de limpieza de datos
# csv  , / ; |
header="dni,nombre,edad,fecha_nacimiento,tarjeta_main,apellido"
rowN="4679797,Gian     ,24,10/10/2000,*******797,gutierrez"
header_tmp=header.split(',')
lista_sucia=rowN.split(',')
for i,j in enumerate(lista_sucia):
    print(i,j)
    lista_sucia[i]=j.strip()
    lista_sucia[i]=lista_sucia[i].upper()
# 2do elemento tiene concatenado con el ultimo
lista_sucia.append(lista_sucia[1]+lista_sucia[-1])
header_tmp.append("fullname")
for i,j in enumerate(header_tmp):
    header_tmp[i]=j.upper()


lista_clean=lista_sucia
print(header_tmp)
print(lista_clean)