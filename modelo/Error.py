class Error():

    
    
    def __init__(self,contador,fila,columna,caracter):
        self.__fila = fila
        self.__columna = columna
        self.__caracter = caracter
        self.__contador = contador

    def getFila(self):
        return self.__fila 
    def setFila(self,fila):
        self.__fila = fila

    def getColumna(self):
        return self.__columna
    def setColumna(self,columna):
        self.__columna = columna

    def getCaracter(self):
        return self.__caracter
    def setCaracter(self,caracter):
        self.__caracter = caracter

    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador = contador

 
    def __str__(self):
        return f"{self.__contador},{self.__fila},{self.__columna},{self.__caracter}"


    

    

        
