from controlador.Archivo import Archivo

class Menu():
    _archivo = Archivo()

    def __init__(self):
        self._archivo = Archivo()



    def menu_Principal(self,almacenado):


        while True:
            try:
                
                print("Proyecto #1 - LFP\n")  
                print("Lenguajes Formales y Programacion A- - JOSE ABRAHAM SOLORZANO HERRERA - 201800937\n")
                print("1. Cargar Archivo")
                print("2. Graficar Ruta")
                print("3. Graficar Mapa")
                print("4. Salir\n")

                numero = int(input("Ingrese un Numero: "))

                if (numero==1):
                    #cargar = Archivo()
                    #almacenado = cargar.cargarArchivo(almacenado)
                    self._archivo.open_File()

                    #break
                elif(numero==2):
                    break
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
                self.menu_Principal(almacenado)


    
