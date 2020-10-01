#                            GUIA
# https://j2logo.com/python/crear-archivo-excel-en-python-con-openpyxl/              
import openpyxl

class Excel():


    def generar_excel(self,almacenado,almacenado2):    

        wb = openpyxl.Workbook()                             # SE CREA UN LIBRO
        hoja = wb.active                                     # SE ACTIVA UNA HOJA
        hoja.title = "Tabla#1 - Error"                       # SE CREA UNA HOJA 
        hoja_token = wb.create_sheet('Tabla#2 - Tokens')     # SE CREA UNA SEGUNDA HOJA


#                       INGRESANDO DATOS EN LA PRIMERA TABLA            
        hoja.append(('No', 'Fila', 'Columna', 'Caracter'))
        
        for linea in almacenado:
            hoja.append([linea.getContador(),linea.getFila(),linea.getColumna(),linea.getCaracter()])

#                       INGRESANDO DATOS EN LA SEGUNDA TABLA            
        hoja_token.append(('No','Lexema','Fila', 'Columna', 'Token'))

        for fila in almacenado2:
            hoja_token.append([fila.getContador(),fila.getLexema(),fila.getFila(),fila.getColumna(),fila.getToken()])

        wb.save('Tabla Error.xlsx')


       



        
