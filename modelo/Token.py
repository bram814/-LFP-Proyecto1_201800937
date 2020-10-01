class Token():

    
    

    

    def __init__(self,contador,lexema,fila,columna,token):
        self.__contador = contador
        self.__fila = fila
        self.__columna = columna
        self.__lexema = lexema
        self.__token = token

    def getContador(self):
        return self.__contador
    def setContador(self,contador):
        self.__contador =  contador

    def getFila(self):
        return self.__fila
    def setFila(self,fila):
        self.__fila = fila
    
    def getColumna(self):
        return self.__columna
    def setColumna(self,columna):
        self.__columna = columna    
    
    def getLexema(self):
        return self.__lexema
    def setLexema(self,lexema):
        self.__lexema = lexema
    
    def getToken(self):
        return self.__token
    def setToken(self,token):
        self.__token = token

    def __str__(self):
        return f'{self.__contador},{self.__lexema},{self.__fila}, {self.__columna},{self.__token}'
