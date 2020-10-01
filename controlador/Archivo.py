from tkinter import filedialog
from controlador.Analizador import Analizador
from io import open

class Archivo():

    analizador_ = Analizador()

    def __init__(self):
        pass

    def open_File(self):
            try:
                #root = Tk()
                ruta =  ""
                filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("TXT files","*.txt"),("all files","*.*")))
                ruta = filename
                if ruta != "":
                    self.cargar_Archivo(ruta)
                    return ruta
                else:
                    
                    return None

            except IndexError as e:
                print(e)   

    def cargar_Archivo(self,ruta):
        print(f"Ruta: {ruta}")
        try:
        
            archivo = open(f"{ruta}","r", encoding="utf-8")
            texto = archivo.readlines()
            archivo.close()
            print(f"Texto:{texto}")
            self.analizador_.metodo_while(texto)

            
        except (FileNotFoundError):
            print("Error")


    