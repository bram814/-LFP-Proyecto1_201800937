from controlador.Archivo import Archivo
from controlador.Graphviz import Graphviz

class Menu():
    _archivo = Archivo()
    ingreso_estacion_inicio = ''
    ingreso_estacion_fin = ''
    _reporte = Graphviz()

    def __init__(self):
        self._archivo = Archivo()
        self.ingreso_estacion_inicio = ''
        self.ingreso_estacion_fin = ''
        self._reporte = Graphviz()



    def menu_Principal(self,lista_ruta,lista_estacion):


        while True:
            try:
                
                print("\nProyecto #1 - LFP\n")  
                print("Lenguajes Formales y Programacion A- - JOSE ABRAHAM SOLORZANO HERRERA - 201800937\n")
                print("1. Cargar Archivo")
                print("2. Graficar Ruta")
                print("3. Graficar Mapa")
                print("4. Salir\n")

                numero = int(input("Ingrese un Numero: "))

                if (numero==1):
                    self._archivo.open_File(lista_ruta,lista_estacion)

                    #break
                elif(numero==2):
                    print('')
                    i = 0
                    while i < len(lista_estacion):
                        print(f'{lista_estacion[i].getNombre()} {lista_estacion[i].getEstado()} {lista_estacion[i].getColor()}')
                        i += 1
                    print('')
                    x = 0
                    while x < len(lista_ruta):
                        print(f'{lista_ruta[x].getNombre()} {lista_ruta[x].getPeso()} {lista_ruta[x].getInicio()} {lista_ruta[x].getFin()}')
                        x += 1      

                    print('\nIngrese el Nombre de la Estacion Inicial: ')
                    self.ingreso_estacion_inicio = input()
                    if(self.verificar_estacion(lista_estacion,self.ingreso_estacion_inicio)==True):

                        print('Ingrese el Nombre de la Estacion Final: ')
                        self.ingreso_estacion_fin = input()
                        if(self.verificar_estacion(lista_estacion,self.ingreso_estacion_fin)==True):
                            print('Todas son validas')
                            #self._reporte.implementacion_ruta(lista_ruta,lista_estacion,self.ingreso_estacion_inicio,self.ingreso_estacion_fin)
                        else:
                            print('Nombre de Estacion Final Incorrecta o esta Cerrada')
                    else:
                        print('Nombre de Estacion Inicial Incorrecta o esta Cerrada')
                    
                elif(numero==3):
                    self._reporte.implementacion_mapa(lista_ruta,lista_estacion)
      
                elif(numero==4):
                    break
                elif(numero<=0 or numero>=5):
                    print("Ingreso un numero menor a 0 o mayor a 4. Debe ser de [1,4]")
                    break
            except:
                print("Ingreso una letra. Debe ser de [1,4]")
                #llamar = Menu()
                #llamar.menuPrincipal(almacenado)
                self.menu_Principal(lista_ruta,lista_estacion)

    def verificar_estacion(self,estacion,entrada):
        x = 0
        verificar = False 
        while x<len(estacion):
            if(estacion[x].getNombre()==entrada and estacion[x].getEstado()=='disponible'):
                verificar = True
                return verificar
            x += 1
        return verificar


    
