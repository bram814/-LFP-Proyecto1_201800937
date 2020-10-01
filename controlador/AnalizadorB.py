from modelo.Station import Station
from modelo.Route import Route
from controlador.Analizador import Analizador

class AnalizadorB():
    
    lista_ruta = list()
    lista_estacion = list()
    lista_analizador = Analizador()


    def __init__(self):
        self.lista_ruta = list()
        self.lista_estacion = list()
        self.lista_analizador = Analizador()

    def metodo_analizador_b(self,texto):
        self.entrada = ''
        self.caracter_actual = ''
        for linea in texto:
            self.entrada += linea

        print('Muestra vector')
        

        x = 0
        while 0 < len(self.entrada):

            self.caracter_actual = self.entrada[x]

            if self.caracter_actual == '<':
                pass

            x += 1

        

    def verificar_expresion(self,texto):
        verificar = True
        return verificar

    def buscar_(self,actual,fin):
        longitud = 0

        while actual < fin :

            actual += 1

        return longitud