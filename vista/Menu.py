from controlador.Archivo import Archivo

class Menu():
    _archivo = Archivo()

    def __init__(self):
        self._archivo = Archivo()



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
                    #print(len(lista_ruta))
                    #print(len(lista_estacion))

                    print('')
                    i = 0
                    while i < len(lista_estacion):
                        print(lista_estacion[i])
                        i += 1
                    
                    x = 0
                    while x < len(lista_ruta):
                        print(lista_ruta[x].getNombre())
                        x += 1  
                elif(numero==3):
                    break
                                         
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


    
