from vista.Menu import Menu
from modelo.Station import Station


almacenado = list()
print(len(almacenado))
menu = Menu()
menu.menu_Principal(almacenado)


#diccionario = dict()

#diccionario[clave] = valor

#{
#    "rutaX":[estadocion1,estacions,3],
#    "rutaY":[estacion3,estacion5,adsffd,sfddf]
#}
def prueba(nombre,estado,color):

    estacion = Station(nombre,estado,color)
    almacenado.append(estacion)
    for value in almacenado:
        print(f"{value.__str__()}")

#for key,value in diccionario.items():
#    if (key = "rutaX"):
#        prin(value)

#prueba("estado1",True,"white")


def get_lista_almacenado():
    return almacenado
#lista_almacenado  = main.get_lista_almacenado()








