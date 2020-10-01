from modelo.Error import Error
from modelo.Token import Token
from controlador.Excel import Excel

class Analizador():
    
    lista_error = list()
    lista_token = list()
    _contador = 0
    _contador2 = 1
    enviar_datos_ = Excel()
    
    
    def __init__(self):
        self._fila  = 1 
        self._columna = 1
        self.lista_error = list()
        self.lista_token = list()
        self._contador = 0
        self._contador2 = 1
        self.enviar_datos_ = Excel()


    #guarda la informacion del archivo en la variable entrada
    def metodo_while(self,texto):
        
        self.entrada = ''
        self.caracter_Actual = ''
        self.lexema = ''
        for linea in texto:
            print(linea)
            self.entrada += linea
        

        x = 0
        while x < len(self.entrada):
            self.caracter_Actual = self.entrada[x]
                        
            if self.caracter_Actual == "<":
                self._columna = 2
                size_lexema = self.get_size_lexema(x)            # x se incrementa 1 para que no tome el valor de <
                self.obtener_error(x+1,x+size_lexema)            # x + size_lexema se incrementa por el valor por que el metodo anterior no lo sumo >
                self.obtener_token(x+1,x+size_lexema)
                x = x + size_lexema                              # x = > TOMA EL VALOR DE x + size_lexema, para continuar despues de >
                self._fila += 1

            elif self.caracter_Actual.isalpha() or self.caracter_Actual.isnumeric():
                pass
            elif self.caracter_Actual == '#' or self.caracter_Actual=="." or self.caracter_Actual==' ':
                pass
            elif self.caracter_Actual == '\n' or self.caracter_Actual=='_':
                pass
            else:
                print(f"Caracter Actual: {self.caracter_Actual} Fila: {self.get_fila(x)} Columna: {self.get_columna(x)}")
                if(self.guardar_error(self.get_fila(x),self.get_columna(x),self.entrada[x])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(x),self.get_columna(x),self.entrada[x])
                                self.lista_error.append(almacenar)
            
            
            x += 1

        self.enviar_datos_.generar_excel(self.lista_error,self.lista_token)
        
            
     #solo funciona para lo que esta dentro de <dsfadfasdfasdf>           
    def obtener_error(self,actual,fin):
        
        #print(f"Actual: {actual} Fin: {fin}")
        while actual < fin:
            c = self.entrada[actual]
            
            if c.isalpha():
                self.lexema += c
                
#                                            <ruta>
                if(c=="r" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='u' and self.entrada[actual+2]=='t' \
                    and self.entrada[actual+3]=='a'):
                    #agregar
                    if(self.entrada[actual-1]!="<"):
                        if(self.entrada[actual-1]!='/'):
                            print(f'1FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                    Error: {self.entrada[actual-1]}')
                            if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                                self.lista_error.append(almacenar)

                elif(c=="a" and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='t' and self.entrada[actual-2]=='u' \
                    and self.entrada[actual-3]=='r'):
                    #agregar
                    if(self.entrada[actual+1]!=">"):
                        print(f'2FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                                Error: {self.entrada[actual+1]}')
                        
                                
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            print('1')
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)
                       
                                


                elif (self.entrada[actual-1]=="<") and (self.entrada[actual]==" "):
                    #agregar
                    print(f'3FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                            Error: {c}')
                    if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),self.entrada[actual])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),self.entrada[actual])
                            self.lista_error.append(almacenar)


                elif (self.entrada[actual]==" " and self.entrada[actual+1]==">"):
                    #agregar
                    print(f'4FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                            Error: {c}')
                    if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),self.entrada[actual])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),self.entrada[actual])
                            self.lista_error.append(almacenar)

                elif c.isupper():
                    print(f'ENCONTRO: {c}')   
                    print(f"               FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                        Error: {self.entrada[actual]}")
                    if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),self.entrada[actual])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),self.entrada[actual])
                            self.lista_error.append(almacenar)

#                                       <ruta>
                elif (self.entrada[actual].isalpha and self.entrada[actual+1]=='>'):

                    if(c!='a' and self.entrada[actual-1]!='t' and self.entrada[actual-2]!='u' and self.entrada[actual-3]!='r' \
                        and c!='e' and self.entrada[actual-1]!='r' and self.entrada[actual-2]!='b' \
                            and c!='o' and self.entrada[actual-1]!='s' \
                                and c!='o' and self.entrada[actual-1]!='i' and self.entrada[actual-2]!="c" and self.entrada[actual-3]!='i' and self.entrada[actual-4]!='n' and self.entrada[actual-5]!='i' \
                                    and c!='n' and self.entrada[actual-1]!='i' and self.entrada[actual-2]!='f'\
                                        and c!='n' and self.entrada[actual-1]!='o' and self.entrada[actual-2]!='i' and self.entrada[actual-3]!='c' and self.entrada[actual-4]!='a' and self.entrada[actual-5]!='t' and self.entrada[actual-6]!='s' and self.entrada[actual-7]!='e' \
                                            and c!='e' and self.entrada[actual-1]!='r' and self.entrada[actual-2]!='b' \
                                                and c!='o' and self.entrada[actual-1]!='d' and self.entrada[actual-2]!='a' and self.entrada[actual-3]!='t' and self.entrada[actual-4]!='s' and self.entrada[actual-5]!='e' \
                                                    and c!='r' and self.entrada[actual-1]!='o' and self.entrada[actual-2]!='l' and self.entrada[actual-3]!='o' and self.entrada[actual-4]!='c'):
                        
                        print(f'5FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                                Error: {c}')
                        if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),self.entrada[actual])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),self.entrada[actual])
                            self.lista_error.append(almacenar)

                elif (self.entrada[actual].isalpha and self.entrada[actual-1]=='<'):

                    if(c!='r' and self.entrada[actual+1]!='u' and self.entrada[actual+2]!='t' and self.entrada[actual+3]!='a' \
                        and c!='n' and self.entrada[actual+1]!='o' and self.entrada[actual+2]!='m' \
                            and c!='p' and self.entrada[actual+1]!='e' \
                                and c!='i' and self.entrada[actual+1]!='n' and self.entrada[actual+2]!="i" and self.entrada[actual+3]!='c' and self.entrada[actual+4]!='i' and self.entrada[actual+5]!='o' \
                                    and c!='f' and self.entrada[actual+1]!='i' and self.entrada[actual+2]!='n'\
                                        and c!='e' and self.entrada[actual+1]!='s' and self.entrada[actual+2]!='t' and self.entrada[actual+3]!='a' and self.entrada[actual+4]!='c' and self.entrada[actual+5]!='i' and self.entrada[actual+6]!='o' and self.entrada[actual+7]!='n' \
                                            and c!='n' and self.entrada[actual+1]!='o' and self.entrada[actual+2]!='m' \
                                                and c!='e' and self.entrada[actual+1]!='s' and self.entrada[actual+2]!='t' and self.entrada[actual+3]!='a' and self.entrada[actual+4]!='d' and self.entrada[actual+5]!='o' \
                                                    and c!='c' and self.entrada[actual+1]!='o' and self.entrada[actual+2]!='l' and self.entrada[actual+3]!='o' and self.entrada[actual+4]!='r'):

                        print(f'6FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                                Error: {c}')
                        if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),self.entrada[actual])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),self.entrada[actual])
                            self.lista_error.append(almacenar)
#                                           </ruta>   
                    
#                                        <nombre>    
                elif(c=="n" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='o'):
                    #agregar
                    if(self.entrada[actual-1]!="<"):
                        if(self.entrada[actual-1]!='/'):
                            print(f'7FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                    Error: {self.entrada[actual-1]}')
                                #agregando    
                            if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                                self.lista_error.append(almacenar)
                    
            
                elif(c=="e" and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='r' \
                    and self.entrada[actual+1]!=">"):
                    #agregar
                    if(self.entrada[actual+1]!=">"):
                        print(f'8FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                                Error: {self.entrada[actual+1]}')
                            #agrengando
                        if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                            self.lista_error.append(almacenar)
                
#                                           <peso>
                elif(c=="p" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='e'):
                    if(self.entrada[actual-1]!="<"):
                        if(self.entrada[actual-1]!='/'):
                            print(f'9FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)}\
                                    Error: {self.entrada[actual-1]}')
                                #agregando
                            if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                                self.lista_error.append(almacenar)
                    
            
                elif(c=="o" and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='s'):
                    #agregar
                    if(self.entrada[actual+1]!=">"):
                        print(f'10FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)}\
                                Error: {self.entrada[actual+1]}')
                            #agregando
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)
                
#                                           <inicio>
                elif(c=="i" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='n'\
                    and self.entrada[actual+2]=="i" and self.entrada[actual+3]=='c' \
                        and self.entrada[actual+4]=="i" and self.entrada[actual+5]=="o"):
                    #agregar
                    if(self.entrada[actual-1]!="<"):
                        if(self.entrada[actual-1]!='/'):
                            print(f'11FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                Error: {self.entrada[actual-1]}')
                                #agrengando
                            if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                                self.lista_error.append(almacenar)
                    
            
                elif(c=="o" and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='i'\
                    and self.entrada[actual-2]=='c' and self.entrada[actual-3]=='i' and self.entrada[actual-4]=='n'\
                        and self.entrada[actual-5]=='i'):
                    #agregar
                    if(self.entrada[actual+1]!=">"):
                        print(f'12FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                            Error: {self.entrada[actual+1]}')
                            #agregando
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)

#                                               <fin>
                elif(c=="f" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='i'\
                    and self.entrada[actual+2]=="n"):
                    #agregar
                    if(self.entrada[actual-1]!="<"):
                        if(self.entrada[actual-1]!='/'):
                            print(f"13FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                Error: {self.entrada[actual-1]}")
                                #agrengando
                            if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                                self._contador += 1
                                almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                                self.lista_error.append(almacenar)
            
                elif(c=="n" and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='i'\
                    and self.entrada[actual-2]=="f"):
                    if(self.entrada[actual+1]!=">"):

                        print(f'14FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                            Error:{self.entrada[actual+1]}')
                            #AGREGANDO
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)

#                                               <estacion>
                elif(c=="e" and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='s' and\
                    self.entrada[actual+2]=='t' and self.entrada[actual+3]=='a' and self.entrada[actual+4]=='c'\
                        and self.entrada[actual+5]=='i' and self.entrada[actual+6]=='o' and self.entrada[actual+7]=='n'):
                    if(self.entrada[actual-1]!='/'):
                        print(f"15FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                    Error: {self.entrada[actual-1]}")
                            #AGREGANDO
                        if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                            self.lista_error.append(almacenar)
                    
                elif(c=='n' and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='o' and \
                    self.entrada[actual-2]=='i' and self.entrada[actual-3]=='c' and self.entrada[actual-4]=='a'\
                        and self.entrada[actual-5]=='t' and self.entrada[actual-6]=='s' \
                            and self.entrada[actual-7]=='e'):
                    if(self.entrada[actual+1]!=">"):
                        print(f"16FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                                    Error: {self.entrada[actual+1]}")
                            #AGREGANDO
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)

#                                           <estado>
                elif(c=='e' and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='s' and \
                    self.entrada[actual+2]=='t' and self.entrada[actual+3]=='a' and self.entrada[actual+4]=='d'\
                        and self.entrada[actual+5]=='o'):
                    if(self.entrada[actual-1]!='/'):
                        print(f"17FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                    Error: {self.entrada[actual-1]}")
                            #agregando
                        if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                            self.lista_error.append(almacenar)
                
                elif(c=='o' and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='d' and \
                    self.entrada[actual-2]=='a' and self.entrada[actual-3]=='t' and self.entrada[actual-4]=='s'\
                        and self.entrada[actual-5]=='e'):
                    if(self.entrada[actual+1]!=">"):
                        print(f"18FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                                    Error: {self.entrada[actual+1]}")
                            #agregando
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)

#                                           <color>
                elif(c=='c' and self.entrada[actual-1].isalpha and self.entrada[actual+1]=='o' and self.entrada[actual+2]=='l' and self.entrada[actual+3]=='o' \
                    and self.entrada[actual+4]=='r'):
                    if(self.entrada[actual-1]!='/'):
                        print(f"19FILA: {self.get_fila(actual-1)} COLUMNA: {self.get_columna(actual-1)} \
                                    Error: {self.entrada[actual-1]}")
                            #agregando
                        if(self.guardar_error(self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual-1),self.get_columna(actual-1),self.entrada[actual-1])
                            self.lista_error.append(almacenar)


                elif(c=='r' and self.entrada[actual+1].isalpha and self.entrada[actual-1]=='o' and self.entrada[actual-2]=='l' and self.entrada[actual-3]=='o' \
                    and self.entrada[actual-4]=='c'):
                    if(self.entrada[actual+1]!=">"):
                        print(f"20FILA: {self.get_fila(actual+1)} COLUMNA: {self.get_columna(actual+1)} \
                                    Error: {self.entrada[actual+1]}")
                            #agregando
                        if(self.guardar_error(self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])==False):
                            self._contador += 1
                            almacenar = Error(self._contador,self.get_fila(actual+1),self.get_columna(actual+1),self.entrada[actual+1])
                            self.lista_error.append(almacenar)

            elif c.isnumeric():
                print(f'22FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                        Error: {c}')
                    #agregando
                if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),c)==False):
                    self._contador += 1
                    almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),c)
                    self.lista_error.append(almacenar)
                
##########################################################################################################################

##########################################################################################################################               
    
            else:

                if(c=='/'   and self.entrada[actual+1]=='r' and self.entrada[actual+2]=='u' and self.entrada[actual+3]=='t' and self.entrada[actual+4]=='a'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='n' and self.entrada[actual+2]=='o' and self.entrada[actual+3]=='m'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='p' and self.entrada[actual+2]=='e' and self.entrada[actual+3]=='s' and self.entrada[actual+4]=='o'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='i' and self.entrada[actual+2]=='n' and self.entrada[actual+3]=='i' and self.entrada[actual+4]=='c' and self.entrada[actual+5]=='i' and self.entrada[actual+6]=='o'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='f' and self.entrada[actual+2]=='i' and self.entrada[actual+3]=='n'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='e' and self.entrada[actual+2]=='s' and self.entrada[actual+3]=='t' and self.entrada[actual+4]=='a' and self.entrada[actual+5]=='c' and self.entrada[actual+6]=='i' and self.entrada[actual+7]=='o' and self.entrada[actual+8]=='n'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='e' and self.entrada[actual+2]=='s' and self.entrada[actual+3]=='t' and self.entrada[actual+4]=='a' and self.entrada[actual+5]=='d' and self.entrada[actual+6]=='o'):
                    pass
                elif(c=='/' and self.entrada[actual+1]=='c' and self.entrada[actual+2]=='o' and self.entrada[actual+3]=='l' and self.entrada[actual+4]=='o' and self.entrada[actual+5]=='r'):
                    pass

                else:
                    print(f'21FILA: {self.get_fila(actual)} COLUMNA: {self.get_columna(actual)} \
                    Error: {c}')
                        #agregando
                    if(self.guardar_error(self.get_fila(actual),self.get_columna(actual),c)==False):
                        self._contador += 1
                        almacenar = Error(self._contador,self.get_fila(actual),self.get_columna(actual),c)
                        self.lista_error.append(almacenar)                    

            self.lexema = ''
            actual += 1
            self._columna += 1
        self._columna = 1

    #RECONOCER FILA Y COLUMNA
    def get_fila(self,actual):
        x = 0
        contador_fila = 1
        while x<actual:
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

    def obtener_token(self,actual,fin):
        while actual<fin:
            c = self.entrada[actual]

            if((c=='r' or c=='R') and (self.entrada[actual+1]=='u' or self.entrada[actual+1]=='U') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'ruta')
            
            elif((c=='n' or c=='N') and (self.entrada[actual+1]=='o' or self.entrada[actual+1]=='O') and (self.entrada[actual+2]=='m' or self.entrada[actual+2]=='M') and (self.entrada[actual+3]=='b' or self.entrada[actual+3]=='B') \
                and (self.entrada[actual+4]=='r' or self.entrada[actual+4]=='R') and (self.entrada[actual+5]=='e' or self.entrada[actual+5]=='E')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3] + self.entrada[actual+4] + self.entrada[actual+5]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'nombre')

            elif((c=='p' or c=='P') and (self.entrada[actual+1]=='e' or self.entrada[actual+1]=='E') and (self.entrada[actual+2]=='s' or self.entrada[actual+2]=='S') and (self.entrada[actual+3]=='o' or self.entrada[actual+3]=='O')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'peso')

            elif((c=='i' or c=='I') and (self.entrada[actual+1]=='n' or self.entrada[actual+1]=='N') and (self.entrada[actual+2]=='i' or self.entrada[actual+2]=='I') and (self.entrada[actual+3]=='c' or self.entrada[actual+3]=='C') \
                and (self.entrada[actual+4]=='i' or self.entrada[actual+4]=='I') and (self.entrada[actual+5]=='O' or self.entrada[actual+5]=='o')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3] + self.entrada[actual+4] + self.entrada[actual+5]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'inicio')

            elif((c=='f' or c=='F') and (self.entrada[actual+1]=='i' or self.entrada[actual+1]=='I') and (self.entrada[actual+2]=='n' or self.entrada[actual+2]=='N')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'fin')

            elif((c=='c' or c=='C') and (self.entrada[actual+1]=='o' or self.entrada[actual+1]=='O') and (self.entrada[actual+2]=='l' or self.entrada[actual+2]=='L') and (self.entrada[actual+3]=='o' or self.entrada[actual+3]=='O') \
                and (self.entrada[actual+4]=='r' or self.entrada[actual+4]=='R')):

                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3] + self.entrada[actual+4]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'color')

            elif((c=='e' or c=='e') and (self.entrada[actual+1]=='s' or self.entrada[actual+1]=='S') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A') \
                and (self.entrada[actual+4]=='d' or self.entrada[actual+4]=='D') and (self.entrada[actual+5]=='o' or self.entrada[actual+5]=='O')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3] + self.entrada[actual+4] + self.entrada[actual+5]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'estado')
            
            elif((c=='e' or c=='E') and (self.entrada[actual+1]=='s' or self.entrada[actual+1]=='S') and (self.entrada[actual+2]=='t' or self.entrada[actual+2]=='T') and (self.entrada[actual+3]=='a' or self.entrada[actual+3]=='A') \
                and (self.entrada[actual+4]=='C' or self.entrada[actual+4]=='c') and (self.entrada[actual+5]=='i' or self.entrada[actual+5]=='I') and (self.entrada[actual+6]=='o' or self.entrada[actual+6]=='O')\
                    and (self.entrada[actual+7]=='n' or self.entrada[actual+7]=='N')):
                
                lexema = c + self.entrada[actual+1] + self.entrada[actual+2] + self.entrada[actual+3] + self.entrada[actual+4] + self.entrada[actual+5] + self.entrada[actual+6] + self.entrada[actual+7]
                self.guardar_token(lexema,self.get_fila(actual),self.get_columna(actual),'estacion')

            actual += 1





    # reccore un contador y para hasta que encuentre >,  por ejemplo empieza con <ruta>
    def get_size_lexema(self,inicio):
        longitud = 0
        for j in range(inicio,len(self.entrada) - 1):

            if self.entrada[j] == ">":
                break
            
            longitud += 1
        return longitud

    def get_size_lexema2(self,inicio):
        longitud = 0
        for j in range(inicio,len(self.entrada) - 1):
            if self.entrada[j] == ">":
                break
            longitud += 1
        return longitud

    def guardar_error(self,fila,columna,caracter):
        
        buscar = False

        x = 0    
        while x < len(self.lista_error):
            
            if(self.lista_error[x].getFila()==fila and self.lista_error[x].getColumna()==columna and self.lista_error[x].getCaracter()==caracter):
                buscar = True
                return buscar
            x += 1

        return buscar

    def guardar_token(self,lexema,fila,columna,token):

        almacenar = Token(self._contador2,lexema,fila,columna,token)
        self.lista_token.append(almacenar)
        self._contador2 += 1