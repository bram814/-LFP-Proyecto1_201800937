from modelo.Station import Station
from modelo.Route import Route
from controlador.Analizador import Analizador

class AnalizadorB():
    
    lista_ruta = list()
    lista_estacion = list()
    lista_analizador = Analizador()
    # atributo <ruta>
    nombre_ruta = ''
    peso_ruta = ''
    inicio_ruta = ''
    fin_ruta = ''
    # atributo <estacion>
    nombre_estacion = ''
    estado_estacion = ''
    color_estacion = ''
    
    def __init__(self):
        self.lista_ruta = list()
        self.lista_estacion = list()
        self.lista_analizador = Analizador()
        self.nombre_ruta = ''
        self.peso_ruta = ''
        self.inicio_ruta = ''
        self.fin_ruta = ''
        self.nombre_estacion = ''
        self.estado_estacion = ''
        self.color_estacion = ''

    def metodo_analizador_b(self,texto):
        self.nombre_ruta = ''
        self.peso_ruta = ''
        self.inicio_ruta = ''
        self.fin_ruta = ''
        self.entrada = ''
        self.caracter_actual = ''
        for linea in texto:
            self.entrada += linea

        x = 1
        print('\n')
        while x < len(self.entrada):

            
            if self.entrada[x] == '<':
                
                size_ = self.obtener_longitud_final(x)                                                      # Encuentra > 5
                
                
                                   #BUSCANDO <ruta>
                if (self.buscar_ruta(x+1,size_+x)==True):
                    print(' <ruta>')                                    
                    x = x + size_                                                                           # Esta en la posicion >                               
                    size_ = self.obtener_longitud_inicial(x)                                                # Encuentra <  
                    x = x + size_                                                                           # Esta en la posicion <
                    if (self.entrada[x]=='<'):
                        size_ = self.obtener_longitud_final(x)                                              # Encuentra >

                                  #1BUSCANDO <nombre>
                        if(self.buscar_nombre(x+1,x+size_)==True):
                            print('     <nombre>')
                            x = x + size_                                                                   # Esta en la posicion >
                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                            self.nombre_indentificador = ''
                            x = x + size_                                                                   # Esta en la posicion <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                    print('     </nombre>')
                                    x = x + size_                                                           # Esta en la posicion >
                                    size_ = self.obtener_longitud_inicial(x)                                # Encuentra <
                                    x = x + size_

                                    if (self.entrada[x]=='<'):

                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >

                                        if (self.buscar_peso(x+1,x+size_)==True):
                                            print('     <peso>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                            self.valor_expresion_peso = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                    print('     </peso>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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

                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                            print('     <inicio>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                    print('     </inicio>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                            print('     <fin>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'fin: {self.verificar_expresion(x+1,x+size_)}')
                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                    print('     </fin>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                        
                        

                        elif(self.buscar_peso(x+1,x+size_)==True):
                            print('     <peso>')
                            x = x + size_                                                                   # Esta en la posicion >
                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                            self.valor_expresion_peso = ''
                            x = x + size_                                                                   # Esta en la posicion <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                    print('     </peso>')
                                    x = x + size_                                                           # Esta en la posicion >
                                    size_ = self.obtener_longitud_inicial(x)                                # Encuentra <
                                    x = x + size_

                                    if (self.entrada[x]=='<'):

                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >

                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                            print('     <nombre>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                            self.nombre_indentificador = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                    print('     </nombre>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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

                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                            print('     <inicio>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                    print('     </inicio>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                            print('     <fin>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'fin: {self.verificar_expresion(x+1,x+size_)}')
                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                    print('     </fin>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                        
                        
                        
                        elif(self.buscar_inicio(x+1,x+size_)==True):
                            print('     <inicio>')
                            x = x + size_                                                                   # Esta en la posicion >
                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                            self.valor_expresion = ''
                            x = x + size_                                                                   # Esta en la posicion <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                    print('     </inicio>')
                                    x = x + size_                                                           # Esta en la posicion >
                                    size_ = self.obtener_longitud_inicial(x)                                # Encuentra <
                                    x = x + size_

                                    if (self.entrada[x]=='<'):

                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >

                                        if (self.buscar_peso(x+1,x+size_)==True):
                                            print('     <peso>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                            self.valor_expresion_peso = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                    print('     </peso>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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

                                        elif (self.buscar_nombre(x+1,x+size_)==True):
                                            print('     <nombre>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                            self.nombre_indentificador = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                    print('     </nombre>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_fin(x+1,x+size_)==True):
                                                            print('     <fin>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                    print('     </fin>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_fin(x+1,x+size_)==True):
                                                                            print('     <fin>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Fin: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                                                    print('     </fin>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                                        elif (self.buscar_fin(x+1,x+size_)==True):
                                            print('     <fin>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'fin: {self.verificar_expresion(x+1,x+size_)}')
                                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                                    print('     </fin>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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


                        elif(self.buscar_fin(x+1,x+size_)==True):
                            print('     <fin>')
                            x = x + size_                                                                   # Esta en la posicion >
                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                            print(f'fin: {self.verificar_expresion(x+1,x+size_)}')
                            self.fin_ruta = self.verificar_expresion(x+1,x+size_)
                            self.valor_expresion = ''
                            x = x + size_                                                                   # Esta en la posicion <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_fin_cierre(x+1,x+size_)==True):
                                    print('     </fin>')
                                    x = x + size_                                                           # Esta en la posicion >
                                    size_ = self.obtener_longitud_inicial(x)                                # Encuentra <
                                    x = x + size_

                                    if (self.entrada[x]=='<'):

                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >

                                        if (self.buscar_peso(x+1,x+size_)==True):
                                            print('     <peso>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                            self.valor_expresion_peso = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                    print('     </peso>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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

                                        elif (self.buscar_nombre(x+1,x+size_)==True):
                                            print('     <nombre>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                            self.nombre_indentificador = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                    print('     </nombre>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_inicio(x+1,x+size_)==True):
                                                            print('     <inicio>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                    print('     </inicio>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_inicio(x+1,x+size_)==True):
                                                                            print('     <inicio>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                                                            self.valor_expresion = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                                                    print('     </inicio>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                                        elif (self.buscar_inicio(x+1,x+size_)==True):
                                            print('     <inicio>')
                                            x = x + size_                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                            print(f'Inicio: {self.verificar_expresion(x+1,x+size_)}')
                                            self.inicio_ruta = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                   # Esta en la posicion <
                                            
                                            if(self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                
                                                if(self.buscar_inicio_cierre(x+1,x+size_)==True):
                                                    print('     </inicio>')
                                                    x = x + size_                                           # Esta en la posicion >
                                                    size_ = self.obtener_longitud_inicial(x)                # Encuentra <
                                                    x = x + size_                                           # Esta en <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)              # Encuentra >

                                                        if (self.buscar_peso(x+1,x+size_)==True):
                                                            print('     <peso>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                            self.valor_expresion_peso = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                    print('     </peso>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                                                            print('     <nombre>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                                            self.nombre_indentificador = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                                    print('     </nombre>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

                                                                                else:
                                                                                    x = x + size_


                                                                        else:
                                                                            x = x + size_

                                                                else:
                                                                    x = x + size_

                                                        elif (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('     <nombre>')
                                                            x = x + size_                                   # Esta en >
                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                            print(f'Nombre: {self.identificador_nombre(x+1,x+size_)}')
                                                            self.nombre_ruta = self.identificador_nombre(x+1,x+size_)
                                                            self.nombre_indentificador = ''
                                                            x = x + size_                                   # Esta en <

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('     </nombre>')
                                                                    x = x + size_                                   # Esta en >
                                                                    size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                    x = x + size_                                   # Esta en <

                                                                    if(self.entrada[x]=="<"):

                                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                        if(self.buscar_peso(x+1,x+size_)==True):
                                                                            print('     <peso>')
                                                                            x = x + size_                                   # Esta en >
                                                                            size_ = self.obtener_longitud_inicial(x)        # Encuentra <
                                                                            print(f'Peso: {self.verificar_ex_peso(x+1,x+size_)}')
                                                                            self.peso_ruta = self.verificar_ex_peso(x+1,x+size_)
                                                                            self.valor_expresion_peso = ''
                                                                            x = x + size_                                   # Esta en <

                                                                            if(self.entrada[x]=='<'):
                                                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                                                if(self.buscar_peso_cierre(x+1,x+size_)==True):
                                                                                    print('     </peso>')
                                                                                    x = x + size_                               # Esta >
                                                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                                                    x = x + size_                               # Esta en <
                                                                                                        
                                                                                    if (self.entrada[x]=='<'):
                                                                                        size_ = self.obtener_longitud_final(x)     # Encuentra >
                                                                                        
                                                                                        if (self.buscar_ruta_cierre(x+1,x+size_)==True):
                                                                                            print(' </ruta>')

                                                                                            print(f'1. {self.nombre_ruta}')
                                                                                            print(f'2. {self.peso_ruta}')
                                                                                            print(f'3. {self.inicio_ruta}')
                                                                                            print(f'4. {self.fin_ruta}\n')
                                                         

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
                elif(self.buscar_estacion(x+1,x+size_)==True):
                    print('     <estacion>')
                    x = x + size_                                                                           # Esta en la posicion >                               
                    size_ = self.obtener_longitud_inicial(x)                                                # Encuentra <  
                    x = x + size_                                                                           # Esta en la posicion <
                    if (self.entrada[x]=='<'):
                        size_ = self.obtener_longitud_final(x)                                              # Encuentra >
                        if (self.buscar_estado(x+1,x+size_)==True):
                            print('             <estado>')
                            x = x + size_                                                                   # Esta >
                            # METODO PARA MOSTRAR ESTADO
                            size_ = self.obtener_longitud_inicial(x)                                                # Encunetra <
                            if(self.verificacion_ex_estado_dos(self.verificacion_ex_estado(x+1,x+size_))==True):
                                print(f'Estado: { self.verificacion_ex_estado(x+1,x+size_).lower()}')
                                self.estado_estacion = self.verificacion_ex_estado(x+1,x+size_).lower()
                            self.verificar_estado = ''
                            x = x + size_                                                                   # Esta <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_estado_cierre(x+1,x+size_)==True):
                                    print('             </estado>')
                                    x = x + size_                                                            # Esta en >
                                    size_ = self.obtener_longitud_inicial(x)                                 # Encuentra <
                                    x = x + size_                                                            # Esta en <

                                    if(self.entrada[x]=='<'):
                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                                                                 
                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                            print('             <nombre>')
                                            x = x + size_                                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                            print(f'Nombre: {self.verificar_expresion(x+1,x+size_)}')
                                            self.nombre_estacion = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                                   # Esta en la posicion <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                                if (self.buscar_nombre_cierre(x+1,size_+x)==True):
                                                    print('             </nombre>')
                                                    x = x + size_                                                           # Esta >
                                                    size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                                    x = x + size_                                                           # Esta <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                        if(self.buscar_color(x+1,x+size_)==True):
                                                            print('             <color>')
                                                            x = x + size_                                                   # >
                                                            size_ = self.obtener_longitud_inicial(x)                                # Encuentra < 
                                                            print(f'Color: {self.verificacion_ex_color(x+1,x+size_)}')
                                                            self.color_estacion = self.verificacion_ex_color(x+1,x+size_)
                                                            self.verificar_color = ''         
                                                            x = x + size_                                                   # <
                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                                if(self.buscar_color_cierre(x+1,x+size_)==True):
                                                                    print('             </color>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                                                    x = x + size_ 

                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)

                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('     </estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')
                                                                else:
                                                                    x = x + size_

                                                        else:
                                                            x = x + size_
                                                else:
                                                    x = x + size_
                                        elif(self.buscar_color(x+1,x+size_)==True):
                                            print('             <color>')
                                            x = x + size_                                   # >
                                            size_ = self.obtener_longitud_inicial(x)        # Ecuentra <
                                            print(f'Color: {self.verificacion_ex_color(x+1,x+size_)}')
                                            self.color_estacion = self.verificacion_ex_color(x+1,x+size_)
                                            self.verificar_color = ''
                                            x = x + size_                                   # <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                if(self.buscar_color_cierre(x+1,x+size_)==True):
                                                    print('             </color>')
                                                    x = x + size_                               # >
                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                    x = x + size_                               # <

                                                    if(self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('             <nombre>')
                                                            x = x + size_
                                                            size_ = self.obtener_longitud_inicial(x)
                                                            print(f'Nombre: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.nombre_estacion = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('             </nombre>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)
                                                                    x = x + size_

                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)
                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('     </estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')

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
##################################################################################3
                        elif (self.buscar_nombre(x+1,x+size_)==True):
                            print('             <nombre>')
                            x = x + size_                                                                   # Esta >
                            size_ = self.obtener_longitud_inicial(x)                                                # Encunetra <
                            print(f'Nombre: {self.verificar_expresion(x+1,x+size_)}')
                            self.nombre_estacion = self.verificar_expresion(x+1,x+size_)
                            self.valor_expresion = ''
                            x = x + size_                                                                   # Esta <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                    print('             </nombre>')
                                    x = x + size_                                                            # Esta en >
                                    size_ = self.obtener_longitud_inicial(x)                                 # Encuentra <
                                    x = x + size_                                                            # Esta en <

                                    if(self.entrada[x]=='<'):
                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                                                                 
                                        if(self.buscar_color(x+1,x+size_)==True):
                                            print('             <color>')
                                            x = x + size_                                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                            print(f'Color: {self.verificacion_ex_color(x+1,x+size_)}')
                                            self.color_estacion = self.verificacion_ex_color(x+1,x+size_)
                                            self.verificar_color = ''
                                            x = x + size_                                                                   # Esta en la posicion <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                                if (self.buscar_color_cierre(x+1,size_+x)==True):
                                                    print('             </color>')
                                                    x = x + size_                                                           # Esta >
                                                    size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                                    x = x + size_                                                           # Esta <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                        if(self.buscar_estado(x+1,x+size_)==True):
                                                            print('             <estado>')
                                                            x = x + size_                                                   # >
                                                            size_ = self.obtener_longitud_inicial(x)                                # Encuentra < 
                                                            if(self.verificacion_ex_estado_dos(self.verificacion_ex_estado(x+1,x+size_))==True):
                                                                print(f'Estado: { self.verificacion_ex_estado(x+1,x+size_).lower()}')
                                                                self.estado_estacion = self.verificacion_ex_estado(x+1,x+size_).lower()
                                                            self.verificar_estado = ''          
                                                            x = x + size_                                                   # <
                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                                if(self.buscar_estado_cierre(x+1,x+size_)==True):
                                                                    print('             </estado>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                                                    x = x + size_                                           # <

                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)
                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('</estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')
                                                                            


                                                                else:
                                                                    x = x + size_

                                                        else:
                                                            x = x + size_
                                                else:
                                                    x = x + size_
                                        elif(self.buscar_estado(x+1,x+size_)==True):
                                            print('             <estado>')
                                            x = x + size_                                   # >
                                            size_ = self.obtener_longitud_inicial(x)        # Ecuentra <
                                            if(self.verificacion_ex_estado_dos(self.verificacion_ex_estado(x+1,x+size_))==True):
                                                print(f'Estado: { self.verificacion_ex_estado(x+1,x+size_).lower()}')
                                                self.estado_estacion = self.verificacion_ex_estado(x+1,x+size_).lower()
                                            self.verificar_estado = ''
                                            x = x + size_                                   # <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                if(self.buscar_estado_cierre(x+1,x+size_)==True):
                                                    print('             </estado>')
                                                    x = x + size_                               # >
                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                    x = x + size_                               # <

                                                    if(self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                        if (self.buscar_color(x+1,x+size_)==True):
                                                            print('             <color>')
                                                            x = x + size_
                                                            size_ = self.obtener_longitud_inicial(x)
                                                            print(f'Color: {self.verificacion_ex_color(x+1,x+size_)}')
                                                            self.color_estacion = self.verificacion_ex_color(x+1,x+size_)
                                                            self.verificar_color = ''
                                                            x = x + size_

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)

                                                                if(self.buscar_color_cierre(x+1,x+size_)==True):
                                                                    print('             </color>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)
                                                                    x = x + size_

                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)
                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('</estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')

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
#########################################
                        elif (self.buscar_color(x+1,x+size_)==True):
                            print('             <color>')
                            x = x + size_                                                                   # Esta >
                            size_ = self.obtener_longitud_inicial(x)                                                # Encunetra <
                            print(f'Color: {self.verificacion_ex_color(x+1,x+size_)}')
                            self.color_estacion = self.verificacion_ex_color(x+1,x+size_)
                            self.verificar_color = ''
                            x = x + size_                                                                   # Esta <

                            if (self.entrada[x]=='<'):
                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                if(self.buscar_color_cierre(x+1,x+size_)==True):
                                    print('             </color>')
                                    x = x + size_                                                            # Esta en >
                                    size_ = self.obtener_longitud_inicial(x)                                 # Encuentra <
                                    x = x + size_                                                            # Esta en <

                                    if(self.entrada[x]=='<'):
                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                                                                 
                                        if(self.buscar_nombre(x+1,x+size_)==True):
                                            print('             <nombre>')
                                            x = x + size_                                                                   # Esta en la posicion >
                                            size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                            print(f'Nombre: {self.verificar_expresion(x+1,x+size_)}')
                                            self.nombre_estacion = self.verificar_expresion(x+1,x+size_)
                                            self.valor_expresion = ''
                                            x = x + size_                                                                   # Esta en la posicion <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)                                      # Encuentra >

                                                if (self.buscar_nombre_cierre(x+1,size_+x)==True):
                                                    print('             </nombre>')
                                                    x = x + size_                                                           # Esta >
                                                    size_ = self.obtener_longitud_inicial(x)                                        # Encuentra <
                                                    x = x + size_                                                           # Esta <

                                                    if (self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)                              # Encuentra >
                                                        if(self.buscar_estado(x+1,x+size_)==True):
                                                            print('             <estado>')
                                                            x = x + size_                                                   # >
                                                            size_ = self.obtener_longitud_inicial(x)                                # Encuentra < 
                                                            if(self.verificacion_ex_estado_dos(self.verificacion_ex_estado(x+1,x+size_))==True):
                                                                print(f'Estado: { self.verificacion_ex_estado(x+1,x+size_).lower()}')
                                                                self.estado_estacion = self.verificacion_ex_estado(x+1,x+size_).lower()
                                                            self.verificar_estado = ''
                                                            x = x + size_                                                   # <
                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)                      # Encuentra >
                                                                if(self.buscar_estado_cierre(x+1,x+size_)==True):
                                                                    print('             </estado>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)                        # Encuentra <
                                                                    x = x + size_                                           # <
                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)
                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('</estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')                                        
                                                                else:
                                                                    x = x + size_

                                                        else:
                                                            x = x + size_
                                                else:
                                                    x = x + size_
                                        elif(self.buscar_estado(x+1,x+size_)==True):
                                            print('             <estado>')
                                            x = x + size_                                   # >
                                            size_ = self.obtener_longitud_inicial(x)        # Ecuentra <
                                            if(self.verificacion_ex_estado_dos(self.verificacion_ex_estado(x+1,x+size_))==True):
                                                print(f'Estado: { self.verificacion_ex_estado(x+1,x+size_).lower()}')
                                                self.estado_estacion = self.verificacion_ex_estado(x+1,x+size_).lower()
                                            self.verificar_estado = ''
                                            x = x + size_                                   # <

                                            if (self.entrada[x]=='<'):
                                                size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                if(self.buscar_estado_cierre(x+1,x+size_)==True):
                                                    print('             </estado>')
                                                    x = x + size_                               # >
                                                    size_ = self.obtener_longitud_inicial(x)    # Encuentra <
                                                    x = x + size_                               # <

                                                    if(self.entrada[x]=='<'):
                                                        size_ = self.obtener_longitud_final(x)      # Encuentra >

                                                        if (self.buscar_nombre(x+1,x+size_)==True):
                                                            print('             <nombre>')
                                                            x = x + size_
                                                            size_ = self.obtener_longitud_inicial(x)
                                                            print(f'Nombre: {self.verificar_expresion(x+1,x+size_)}')
                                                            self.nombre_estacion = self.verificar_expresion(x+1,x+size_)
                                                            self.valor_expresion = ''
                                                            x = x + size_

                                                            if(self.entrada[x]=='<'):
                                                                size_ = self.obtener_longitud_final(x)

                                                                if(self.buscar_nombre_cierre(x+1,x+size_)==True):
                                                                    print('             </nombre>')
                                                                    x = x + size_
                                                                    size_ = self.obtener_longitud_inicial(x)
                                                                    x = x + size_
                                                                    if(self.entrada[x]=='<'):
                                                                        size_ = self.obtener_longitud_final(x)
                                                                        if(self.buscar_estacion_cierre(x+1,x+size_)==True):
                                                                            print('</estacion>')
                                                                            print(f'1. {self.nombre_estacion}')
                                                                            print(f'2. {self.estado_estacion}')
                                                                            print(f'3. {self.color_estacion}')
                                                                            

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
                        
#####################################################3                        
                        else:
                            x = x + size_
                else:
                    x = x + size_                                              # size_ + x ==== esta en la posicion >       
            
            #print(f'                REVISANDO: {self.entrada[x]} {self.entrada[x-1]} {self.entrada[x+1]}')
            x += 1

#                                   VERIFICACION ESTADO
    def verificacion_ex_estado(self,actual,fin):
        self.verificar_estado = ''
        while actual < fin :
            c = self.entrada[actual]
            if(c.isalpha() or c.isupper()):
                self.verificar_estado += c
            else:
                return self.verificar_estado
            actual += 1
        return self.verificar_estado
    
    def verificacion_ex_estado_dos(self,temporal):
        validar = False
        if(temporal.lower() =='disponible' or temporal.lower() == 'cerrada'):
            validar = True
            return validar
        return validar
#                                   VERIFICACION COLOR

    def verificacion_ex_color(self,actual,fin):
        self.verificar_color = ''
        while actual < fin :
            c = self.entrada[actual]
            if(c=='#'):
                if(self.entrada[actual+1].isalpha() or self.entrada[actual+1].isnumeric() or self.entrada[actual+1].isupper()):
                    self.verificar_color += c
                    if(self.verificar_ex_color_dos(actual+1,fin)!=' '):
                        return self.verificar_color
            actual += 1
        return self.verificar_color
    
    def verificar_ex_color_dos(self,actual,fin):
        while actual < fin:
            c = self.entrada[actual]
            if(c.isalpha()):
                self.verificar_color += c
            elif(c.isnumeric()):
                self.verificar_color += c
            elif(c.isupper()):
                self.verificar_color += c
            else:
                break
            actual += 1
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
#                                   VERIFICAR IDENTIFICADOR
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
                 
                if(self.entrada[actual-1].isalpha() or self.entrada[actual-1]=='_' or self.entrada[actual-1].isnumeric() or self.entrada[actual-1].isupper()):
                    self.valor_expresion += str(self.entrada[actual])
                      
            else:
                break
            
            actual += 1
        return self.valor_expresion
#                                         IDENTIFICADOR PARA NOMBRE
    def identificador_nombre(self,actual,fin):
        self.nombre_indentificador = ''
        while actual < fin:
            if(self.entrada[actual].isalpha() or self.entrada[actual].isupper()):
                if (actual + 1)==fin:
                    self.nombre_indentificador += self.entrada[actual]
                    return self.nombre_indentificador
                else:
                    self.nombre_indentificador += self.entrada[actual]
                    
                    if(self.identificador_nombre_dos(actual+1,fin)!=' '):
                        return self.nombre_indentificador
                        

            actual += 1
        return self.nombre_indentificador

    def identificador_nombre_dos(self,actual,fin):
        
        while actual < fin:
            if (self.entrada[actual].isalpha() or self.entrada[actual]=='_' or self.entrada[actual].isnumeric() or self.entrada[actual].isupper() or self.entrada[actual]=='@' or self.entrada[actual]=='#'):
                 
                if(self.entrada[actual-1].isalpha() or self.entrada[actual-1]=='_' or self.entrada[actual-1].isnumeric() or self.entrada[actual-1].isupper() or self.entrada[actual-1]=='@' or self.entrada[actual-1]=='#'):
                    self.nombre_indentificador += str(self.entrada[actual])
                      
            else:
                break
            
            actual += 1
        return self.nombre_indentificador

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
#                                   VERIFICACION </ruta>
    def buscar_ruta_cierre(self,actual,fin):
        valor_ruta_cierre = False
        while actual < fin :
            c = self.entrada[actual]
            if(c=='/'):
                valor_ruta_cierre = self.buscar_ruta(actual+1,fin)
                return valor_ruta_cierre
            actual += 1    
        return valor_ruta_cierre
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
#                                   VERIFICACION </nombre>
    def buscar_nombre_cierre(self,actual,fin):
        valor_nombre_cierre = False
        while actual < fin :
            c = self.entrada[actual]

            if (c == '/'):
                valor_nombre_cierre = self.buscar_nombre(actual+1,fin)
                return valor_nombre_cierre

            actual += 1
        return valor_nombre_cierre

#                                   VERIFICAR <peso>

    def buscar_peso(self,actual,fin):
        valor_peso = False
        while actual < fin:
            c =  self.entrada[actual]
            if((c=='p' or c=='P') and (self.entrada[actual+1]=='e' or self.entrada[actual+1]=='E') and (self.entrada[actual+2]=='s' or self.entrada[actual+2]=='S') and (self.entrada[actual+3]=='o' or self.entrada[actual+3]=='O')):
                valor_peso = True
                return valor_peso
            actual += 1
#                                   VERIFICAR </peso>                            
    def buscar_peso_cierre(self,actual,fin):
        valor_peso_cierre = False
        while actual < fin:
            c = self.entrada[actual]
            if(c=='/'):
                valor_peso_cierre = self.buscar_peso(actual+1,fin)
                return valor_peso_cierre
            actual += 1
        return valor_peso_cierre

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
#                                   VERIFICAR </inicio>
    def buscar_inicio_cierre(self,actual,fin):
        valor_inicio_cierre = False
        while actual < fin:
            c = self.entrada[actual]
            if (c=='/'):
                valor_inicio_cierre = self.buscar_inicio(actual+1,fin)
                return valor_inicio_cierre
            actual += 1
        return valor_inicio_cierre
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
#                                   VERIFICAR </fin>
    def buscar_fin_cierre(self,actual,fin):
        valor_fin_cierre = False
        while actual < fin :
            c = self.entrada[actual]
            if(c=='/'):
                valor_fin_cierre = self.buscar_fin(actual+1,fin)
                return valor_fin_cierre
            actual += 1
        return valor_fin_cierre

#                                   VERIFICAR <estacion>

    def buscar_estacion(self,actual,fin):
        valor_estacion = False
        while actual < fin:
            c = self.entrada[actual]
            if((c=='e' or c=='E') and (self.entrada[actual+1]=='s' or self.entrada[actual+1]=='S') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A') \
                and (self.entrada[actual+4]=='C' or self.entrada[actual+4]=='c') and (self.entrada[actual+5]=='i' or self.entrada[actual+5]=='I') and (self.entrada[actual+6]=='o' or self.entrada[actual+6]=='O')\
                    and (self.entrada[actual+7]=='n' or self.entrada[actual+7]=='N')):
                    valor_estacion = True
                    return valor_estacion
            actual += 1
        return valor_estacion
#                                   VERIFICACION </estacion>
    def buscar_estacion_cierre(self,actual,fin):
        valor_estacion_cierre = False
        while actual < fin:
            c = self.entrada[actual]
            if(c=='/'):
                valor_estacion_cierre = self.buscar_estacion(actual+1,fin)
                return valor_estacion_cierre
            actual += 1
        return valor_estacion_cierre
#                                   VERIFICAR <estado>
    def buscar_estado(self,actual,fin):
        valor_estado = False
        while actual < fin:
            c = self.entrada[actual]
            if((c=='e' or c=='e') and (self.entrada[actual+1]=='s' or self.entrada[actual+1]=='S') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A') \
                and (self.entrada[actual+4]=='d' or self.entrada[actual+4]=='D') and (self.entrada[actual+5]=='o' or self.entrada[actual+5]=='O')):
                valor_estado = True
                return valor_estado
            actual += 1
        return valor_estado
#                                   VERIFICAR </estado>
    def buscar_estado_cierre(self,actual,fin):
        valor_estado_cierre = False
        while actual < fin :
            c = self.entrada[actual]
            if (c=='/'):
                valor_estado_cierre = self.buscar_estado(actual+1,fin)
                return valor_estado_cierre
            actual += 1
        return valor_estado_cierre
#                                   VERIFICAR <color>
    def buscar_color(self,actual,fin):
        valor_color = False
        while actual < fin :
            c = self.entrada[actual]
            if((c=='c' or c=='C') and (self.entrada[actual+1]=='o' or self.entrada[actual+1]=='O') and (self.entrada[actual+2]=='l' or self.entrada[actual+2]=='L') and (self.entrada[actual+3]=='o' or self.entrada[actual+3]=='O') \
                and (self.entrada[actual+4]=='r' or self.entrada[actual+4]=='R')):
                valor_color = True
                return valor_color
            actual += 1
        return valor_color
#                                   VERIFICAR </color>
    def buscar_color_cierre(self,actual,fin):
        valor_color_cierre = False
        while actual < fin:
            c = self.entrada[actual]
            if(c=='/'):
                valor_color_cierre = self.buscar_color(actual+1,fin)
                return valor_color_cierre
            actual += 1
        
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
        while actual < len(self.entrada): 
            #c = self.entrada[actual]
            #print(f"Valor C-: {c}")  
            if (self.entrada[actual]=='<'):
                break
            longitud += 1
            actual += 1
        return longitud
