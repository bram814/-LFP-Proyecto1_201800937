

class Station():

    __nombre = None
    __estado = None
    __color = None


    def __init__(self,nombre,estado,color):
        self.__nombre = nombre
        self.__estado = estado
        self.__color = color

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getEstado(self):
        return self.__estado
    def setEstado(self,_estado):
        self.__estado = _estado

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color     

    def __str__(self):
        return "Nombre de Estacion: " + self.__nombre + "; Estado: " +  self.__estado  +\
            "; Color: " + self.__color 