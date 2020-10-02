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
        self.nombre_ruta = ''
        self.peso_ruta = 0
        self.inicio_ruta = ''
        self.fin_ruta = ''
        self.entrada = ''
        self.caracter_actual = ''
        for linea in texto:
            self.entrada += linea

        x = 1
        print('')
        while x < len(self.entrada):

            
            if self.entrada[x] == '<':
                
                size_ = self.obtener_longitud_final(x)                                                      # Encuentra > 5
                
                
                                   #BUSCANDO <ruta>
                if (self.buscar_ruta(x+1,size_+x)==True):
                    print('encontro ruta')                                    
                    x = x + size_                                                                           # Esta en la posicion >                               
                    size_ = self.obtener_longitud_inicial(x)                                                # Encuentra <  
                    x = x + size_                                                                           # Esta en la posicion <
                    if (self.entrada[x]=='<'):
                        size_ = self.obtener_longitud_final(x)                                              # Encuentra >

                                  #1BUSCANDO <nombre>
                        if(self.buscar_nombre(x+1,x+size_)==True):
                            print('encontro nombre')
                            x = x + size_                                                                   # Esta en la posicion >
                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                            print(f'Valor Correcto1: {self.verificar_expresion(x+1,x+size_)}')
                            self.valor_expresion = ''
                            x = x + size_                                                                   # Esta en la posicion <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_nombre(x+1,x+size_)==True):
                                    print('encontro nombre')
                                    x = x + size_                                                           # Esta en la posicion >
                                    size_ = self.obtener_longitud_inicial(x)                                # Encuentra <
                                    x = x + size_

                                    if (self.entrada[x]=='<'):

                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >

                                        if (self.buscar_peso(x+1,x+size_)==True):
                                            print('encontro peso')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Valor Correcto2: {self.verificar_ex_peso(x+1,x+size_)}')
                                            self.valor_expresion_peso = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_peso(x+1,x+size_)==True):
                                                    print('encontro peso')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('encontro inicio')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Valor Correcto3: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio(x+1,x+size_)==True):
                                                                    print('encontro inicio')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('encontro fin')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Valor Correcto4: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin(x+1,x+size_)==True):
                                                                                    print('encontro fin')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_




                                                                    

                                                                else:
                                                                    x = x + size_

                                                        else:
                                                            x = x + size_       
                                                else:
                                                    x = x + size_
                                        else:
                                            x = x + size_
                                else:
                                    x = x + size_
                        else:   
                            x = x + size_
                     

                                   #BUSCANDO <estacion>
                
                
                x = x + size_-1                                              # size_ + x ==== esta en la posicion >       
            
            x += 1
#                                   VERIFICAR PESO DE RUTA

    def verificar_ex_peso(self,actual,fin):
        self.valor_expresion_peso = ''
        while actual < fin: 
            c = self.entrada[actual]
            
            if (c.isnumeric()):
                if(actual+1)==fin:
                    self.valor_expresion_peso += str(c)
                    return self.valor_expresion_peso
                else:
                    self.valor_expresion_peso += str(self.entrada[actual])
                    if(self.entrada[actual+1].isnumeric()):
                        if(self.verificar_ex_peso_sin_punto(actual+1,fin)!=' '):
                            return self.valor_expresion_peso
                    elif(self.entrada[actual+1]=='.'):
                        self.valor_expresion_peso += str(self.entrada[actual+1])
                        if (self.verficar_ex_peso_con_punto(actual+2,fin)!=' '):
                            return self.valor_expresion_peso
                        
                    return self.valor_expresion_peso
            elif (c=='.'):
                if(actual+1)==fin:
                    self.valor_expresion_peso += str(0) + c + str(0)
                    return self.valor_expresion_peso
                else:
                    self.valor_expresion_peso += str(0) + c
                    if (self.verficar_ex_peso_con_punto(actual+1,fin)!=' '):
                        return self.valor_expresion_peso
            actual += 1

    def verficar_ex_peso_con_punto(self,actual,fin):
        while actual < fin:
            if (self.entrada[actual].isnumeric()):
                self.valor_expresion_peso += str(self.entrada[actual])
            elif (self.entrada[actual]=='.'):
                break
            else:
                break
            actual += 1

    def verificar_ex_peso_sin_punto(self,actual,fin):
        while actual < fin :
            if (self.entrada[actual].isnumeric()):

                if(self.entrada[actual+1].isnumeric()):
                    self.valor_expresion_peso += str(self.entrada[actual])

                elif(self.entrada[actual+1]=='.'):
                    self.valor_expresion_peso += str(self.entrada[actual+1])
                    if (self.verficar_ex_peso_con_punto(actual+2,fin)!=' '):
                        break
                else: 
                    break
                
            actual += 1
#                                   VERIFICAR EXPRESION
    def verificar_expresion(self,actual,fin):
        self.valor_expresion = ''
        while actual < fin:
            if(self.entrada[actual].isalpha() or self.entrada[actual].isupper()):
                if (actual + 1)==fin:
                    self.valor_expresion += self.entrada[actual]
                    return self.valor_expresion
                else:
                    self.valor_expresion += self.entrada[actual]
                    
                    if(self.verificar_expresion_dos(actual+1,fin)!=' '):
                        return self.valor_expresion
                        

            actual += 1
        return self.valor_expresion

    def verificar_expresion_dos(self,actual,fin):
        
        while actual < fin:
            if (self.entrada[actual].isalpha() or self.entrada[actual]=='_' or self.entrada[actual].isnumeric() or self.entrada[actual].isupper()):
                 
                if(self.entrada[actual-1].isalpha() or self.entrada[actual-1]=='_' or self.entrada[actual-1].isnumeric() or self.entrada[actual].isupper()):
                    self.valor_expresion += str(self.entrada[actual])
                      
            else:
                break
            
            actual += 1
        return self.valor_expresion
#                                   VERIFICAR   <ruta>
    def buscar_ruta(self,actual,fin):
        valor_ruta = False

        while actual < fin :
            c = self.entrada[actual]

            if((c=='r' or c=='R') and (self.entrada[actual+1]=='u' or self.entrada[actual+1]=='U') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A')):
                valor_ruta = True
                return valor_ruta
            actual += 1 
        
        return valor_ruta
#                                   VERIFICAR   <nombre>
    def buscar_nombre(self,actual,fin):
        valor_nombre = False

        while actual < fin:
            c = self.entrada[actual]
            if((c=='n' or c=='N') and (self.entrada[actual+1]=='o' or self.entrada[actual+1]=='O') and (self.entrada[actual+2]=='m' or self.entrada[actual+2]=='M') and (self.entrada[actual+3]=='b' or self.entrada[actual+3]=='B') \
                and (self.entrada[actual+4]=='r' or self.entrada[actual+4]=='R') and (self.entrada[actual+5]=='e' or self.entrada[actual+5]=='E')):
                valor_nombre = True
                return valor_nombre


           
            actual += 1

        return valor_nombre
#                                   VERIFICAR <peso>

    def buscar_peso(self,actual,fin):
        valor_peso = False
        while actual < fin:
            c =  self.entrada[actual]
            if((c=='p' or c=='P') and (self.entrada[actual+1]=='e' or self.entrada[actual+1]=='E') and (self.entrada[actual+2]=='s' or self.entrada[actual+2]=='S') and (self.entrada[actual+3]=='o' or self.entrada[actual+3]=='O')):
                valor_peso = True
                return valor_peso
            actual += 1
#                                   VERIFICAR <inicio>

    def buscar_inicio(self,actual,fin):
        valor_inicio = False

        while actual < fin:
            c = self.entrada[actual]
            
            if((c=='i' or c=='I') and (self.entrada[actual+1]=='n' or self.entrada[actual+1]=='N') and (self.entrada[actual+2]=='i' or self.entrada[actual+2]=='I') and (self.entrada[actual+3]=='c' or self.entrada[actual+3]=='C') and (self.entrada[actual+4]=='i' or self.entrada[actual+4]=='I') and (self.entrada[actual+5]=='O' or self.entrada[actual+5]=='o')):
                valor_inicio = True
                return valor_inicio
            actual += 1
            
        return valor_inicio

#                                   VERIFICAR <fin>

    def buscar_fin(self,actual,fin):
        valor_fin = False
        while actual < fin:
            c = self.entrada[actual]
            if((c=='f' or c=='F') and (self.entrada[actual+1]=='i' or self.entrada[actual+1]=='I') and (self.entrada[actual+2]=='n' or self.entrada[actual+2]=='N')):
                valor_fin = True
                return valor_fin
            actual += 1
        return valor_fin
#                           obtiene la cantidad entre < >
    def obtener_longitud_final(self,actual):
        longitud = 0
        while actual < len(self.entrada):   
            #c = self.entrada[actual]
            #print(f"Valor C+: {c}")
            if (self.entrada[actual]=='>'):
                break
            longitud += 1
            actual += 1
        return longitud

    def obtener_longitud_inicial(self,actual):
        longitud = 0
        print(self.entrada[actual])
        while actual < len(self.entrada): 
            #c = self.entrada[actual]
            #print(f"Valor C-: {c}")  
            if (self.entrada[actual]=='<'):
                break
            longitud += 1
            actual += 1
        return longitud

#                               RECONOCER FILA Y COLUMNA
    def get_fila(self,actual):
        x = 0
        contador_fila = 1
        while x < actual:
            c = self.entrada[x]
            if(c =="\n"):
                contador_fila += 1
            x += 1
        return contador_fila        

    def get_columna(self,actual):
        x=0
        contador_columna = 1
        while x<actual:
            c = self.entrada[x]
            contador_columna += 1
            if(c == '\n'):
                contador_columna = 1
            elif (x+1 == actual):
                return contador_columna
            x += 1
                       