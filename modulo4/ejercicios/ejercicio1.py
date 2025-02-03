ruta='/workspaces/workspacepy0125v2/modulo4/files/demo.txt'
baseRuta='/workspaces/workspacepy0125v2/modulo4/files/'
salto ='\n'
#rutawindows='C:\\Users\\User\\nando\\torres\\basico'

with open(ruta,mode='w') as file:
    file.write('escribiendo22323131')


for i in range(2012,2014):
    newRuta=f"{baseRuta}{i}-v1.txt"
    f =open(newRuta,mode='a') 
    texto=f'\neste es el reporte {i}'
    f.write(texto)