
class Route():

    __nombre = None
    __peso = 0
    __inicio = None
    __fin = None

    def __init__(self,nombre,peso,inicio,fin):
        self.__nombre = nombre
        self.__peso = peso
        self.__inicio = inicio
        self.__fin = fin 

    def getNombre(self):
        return self.__nombre 
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getPeso(self):
        return self.__peso 
    def setPeso(self,peso):
        self.__peso = peso
    
    def getInicio(self):
        return self.__inicio
    def setInicio(self,peso):
        self.__peso = peso
    
    def getFin(self):
        return self.__fin
    def setFin(self,fin):
        self.__fin = fin
    

    def __str__(self):
        return "Nombre de Ruta: " +self.__nombre + "; Peso: " + self.__inicio + "; Inicio: " + self.__inicio \
            + "; Fin: " + self.__fin



