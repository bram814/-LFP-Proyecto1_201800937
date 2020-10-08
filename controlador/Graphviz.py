from graphviz import Digraph

class Graphviz():
    lista_graph = []
    lista_graph_final = []
    lista_graph_node = []
    lista_clasificar = []

    def __init__(self):
        self.lista_graph = []
        self.lista_graph_final = []
        self.lista_graph_node = []


    def implementacion_mapa(self,lista_ruta,lista_estacion):
        f = Digraph(format='png', name='Reporte_Mapa')
        f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
        f.attr('node', shape='circle')

        for linea in lista_estacion:
            if (self._estacion_(lista_estacion,linea.getNombre())==True):
                f.node(f'{linea.getNombre()}\n{linea.getEstado()}', style='filled',fillcolor=f'{linea.getColor()}')

        for linea in lista_ruta:
            if (self._estacion_(lista_estacion,linea.getInicio())==True):
                if (self._estacion_(lista_estacion,linea.getFin())==True):
                    f.edge(f'{self.verificar_estacion(lista_estacion,linea.getInicio())}', f'{self.verificar_estacion(lista_estacion,linea.getFin())}', label=f'{linea.getNombre()}\n{linea.getPeso()}') 
        f.view()


    def implementacion_ruta(self,lista_ruta,lista_estacion,inicio,fin):

        for linea in lista_ruta:
            if(linea.getInicio().lower() == inicio.lower()): # POR MEDIO DEL INICIO DE LA ESTACION, VERIFICARA EN LA RUTA SI COINCIDE EL INICIO DE LA RUTA O EL FIN.
                if(self.verificar_graph(linea.getNombre())==False):     # combrueba si en esa lista ya existe esa ruta.
                    if(self._estacion_(lista_estacion,linea.getInicio())==True):
                        if(self._estacion_(lista_estacion,linea.getFin())==True):
                            self.lista_graph.append(linea.getNombre())


        for linea in lista_ruta:
            if(linea.getFin().lower() == fin.lower()): # POR MEDIO DEL INICIO DE LA ESTACION, VERIFICARA EN LA RUTA SI COINCIDE EL INICIO DE LA RUTA O EL FIN.
                if(self.verificar_graph_final(linea.getNombre())==False):     # combrueba si en esa lista ya existe esa ruta.
                    if(self._estacion_(lista_estacion,linea.getInicio())==True):
                        if(self._estacion_(lista_estacion,linea.getFin())==True):
                            self.lista_graph_final.append(linea.getNombre())
   
        print('\nRutas 1')
        for a in self.lista_graph:
            print(a)
        print('\nRutas 2')
        for b in self.lista_graph_final:
            print(b)


        self.comprobar_peso_inicial(lista_ruta,lista_estacion,inicio,fin)

        self.lista_graph = []
        self.lista_graph_final = []
        self.lista_graph_node = []
        self.lista_clasificar = []
        


    def comprobar_peso_inicial(self,lista_ruta,lista_estacion,inicio,fin):
        peso_temporal = 0
        ruta_temportal = ''
        aux = 0
        aux_ruta = ''
        i = 0 
        while i < len(self.lista_graph):

            if(self.verificar_ruta_inicio(lista_ruta,self.lista_graph[i]).lower()==inicio.lower()): # Obtiene la estacion de inicio
                    if(peso_temporal==0):
                        peso_temporal = self.traer_peso(lista_ruta,self.lista_graph[i])
                        ruta_temportal = self.lista_graph[i]
                    else:
                        aux = self.traer_peso(lista_ruta,self.lista_graph[i])
                        aux_ruta = self.lista_graph[i]

                        if (aux < peso_temporal):
                            temp = peso_temporal
                            temp_ruta = ruta_temportal

                            peso_temporal = aux
                            ruta_temportal = aux_ruta
                            
                            aux = temp
                            aux_ruta = temp_ruta 

            i += 1

        print(f'\nmenor: {peso_temporal}, {ruta_temportal}')
        print(f'mayor: {aux}, {aux_ruta}')


        peso_temporal_final = 0
        ruta_temportal_final = ''
        aux_final = 0
        aux_ruta_final = ''
        x = 0
        while x < len(self.lista_graph_final):

            if(self.verificar_ruta_fin(lista_ruta,self.lista_graph_final[x]).lower()==fin.lower()): # Obtiene la estacion de inicio
                    if(peso_temporal_final==0):
                        peso_temporal_final = self.traer_peso(lista_ruta,self.lista_graph_final[x])
                        ruta_temportal_final = self.lista_graph_final[x]
                    else:
                        aux_final = self.traer_peso(lista_ruta,self.lista_graph_final[x])
                        aux_ruta_final = self.lista_graph_final[x]

                        if (aux_final < peso_temporal_final):
                            temp = peso_temporal_final
                            temp_ruta = ruta_temportal_final

                            peso_temporal_final = aux_final
                            ruta_temportal_final = aux_ruta_final
                            
                            aux_final = temp
                            aux_ruta_final = temp_ruta 

            x += 1
        print(f'\nmenor: {peso_temporal_final}, {ruta_temportal_final}')
        print(f'mayor: {aux_final}, {aux_ruta_final}')
        
        self.lista_clasificar.append(ruta_temportal)
        self.lista_clasificar.append(ruta_temportal_final)

        bx = Digraph(format='png', name='Reporte_Mapa')
        bx.attr(rankdir='LR', size='9')    # PARA QUE SEA HORIZONTAL
        bx.attr('node', shape='circle')

        for linea in lista_estacion:
            if (self._estacion_(lista_estacion,linea.getNombre())==True):
                bx.node(f'{linea.getNombre()}\n{linea.getEstado()}', style='filled',fillcolor=f'{linea.getColor()}')

        for linea in lista_ruta:
            if(self.verificar_clasificados(linea.getNombre())==True):
                if (self._estacion_(lista_estacion,linea.getInicio())==True):
                    if (self._estacion_(lista_estacion,linea.getFin())==True):
                        bx.edge(f'{self.verificar_estacion(lista_estacion,linea.getInicio())}', f'{self.verificar_estacion(lista_estacion,linea.getFin())}', label=f'{linea.getNombre()}\n{linea.getPeso()}') 
        bx.view()

    def verificar_clasificados(self,nombre):
        x = 0 
        validar = False
        while x < len(self.lista_clasificar):
            if(self.lista_clasificar[x].lower()==nombre.lower()):
                validar = True
                return validar 
            x += 1
   

#  VA A VERIFICAR SI EL NOMBRE DE LA RUTA EXISTE EN LA LISTA INICIAL DE GRAFO, Y TRAE LA ESTACION INICIO
    def verificar_ruta_inicio(self,ruta,entrada):
        x = 0
        verificar = ''
        while x<len(ruta):
            if(ruta[x].getNombre().lower()==entrada.lower()):
                verificar = ruta[x].getInicio()
                return verificar
            x += 1
        return verificar
    
# VA A VERIFICAR SI EL NOMBRE DE LA RUTA EXISTE EN LA LISTA FINAL DEL GRAFO
    def verificar_ruta_fin(self,ruta,entrada):
        x = 0
        verificar = 0 
        while x<len(ruta):
            if(ruta[x].getNombre().lower()==entrada.lower()):
                verificar = ruta[x].getFin()
                return verificar
            x += 1
        return verificar

# POR MEDIO DE LA LISTA RUTA VERIFICA SI SON IGUALES EN LA LISTA GRAFO Y VA A TRAER EL PESO DE LA RUTA
    def traer_peso(self,ruta,entrada):
        x = 0
        peso = 0 
        while x<len(ruta):
            if(ruta[x].getNombre().lower()==entrada.lower()):
                peso = ruta[x].getPeso()
                return peso
            x += 1
        return peso


    def verificar_graph(self,nombre):
        x = 0
        validar = False
        while x < len(self.lista_graph):
            if(self.lista_graph[x].lower()==nombre.lower()):
                validar = True
                return validar
            x += 1
        return validar
    
    def verificar_graph_final(self,nombre):
        x = 0
        validar = False
        while x < len(self.lista_graph_final):
            if(self.lista_graph_final[x].lower()==nombre.lower()):
                validar = True
                return validar
            x += 1
        return validar

    def verificar_node(self,nombre):
        x = 0
        validar = False
        while x < len(self.lista_graph_node):
            if(self.lista_graph_node[x].lower()==nombre.lower()):
                validar = True
                return validar
            x += 1
        return validar

    def verificar_estacion(self,estacion,entrada):
        x = 0
        verificar = '' 
        while x<len(estacion):
            if(estacion[x].getNombre().lower()==entrada.lower() and estacion[x].getEstado()=='disponible'):
                verificar = f'{estacion[x].getNombre()}\n{estacion[x].getEstado()}'
                return verificar
            x += 1
        return verificar

    def _estacion_(self,estacion,entrada):
        x = 0
        verificar = False 
        while x<len(estacion):
            if(estacion[x].getNombre().lower()==entrada.lower() and estacion[x].getEstado()=='disponible'):
                verificar = True
                return verificar
            x += 1
        return verificar

    def buscar_ruta(self,inicio):
        x = 0
        validar = False
        while x < len(self.lista_graph):
            if(self.lista_graph[x]==inicio):
                validar = True
                return validar
            x += 1
        return validar