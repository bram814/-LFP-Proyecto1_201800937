

class Station():

    __nombre = None
    __estado = True
    __color = None


    def __init__(self,nombre,estado,color):
        self.__nombre = nombre
        self.__estado = estado
        self.__color = color

    def state(self,estado):
        if(estado=="disponible"):
            self.__estado = True
            actual = self.__estado
            return actual

        elif(estado=="cerrada"):
            self.__estado = False
            actual = self.__estado
            return actual


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
        if (self.__estado):
            return "Nombre de Estacion: " + self.__nombre + "; Estado: TRUE "  +\
                "; Color: " + self.__color 
        else:
            return "Nombre de Estacion: " + self.__nombre + "; Estado: Falso "  +\
                "; Color: " + self.__color 