from graphviz import Digraph

class Graphviz():
    lista_graph = []

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
        f = Digraph(format='png', name='Reporte_Ruta')
        f.attr(rankdir='LR', size='9')    # PARA QUE SEA HORIZONTAL
        f.attr('node', shape='circle')


    def verificar_ruta(self,ruta,entrada):
        x = 0
        verificar = False 
        while x<len(ruta):
            if(ruta[x].getNombre().lower()==entrada.lower()):
                verificar = True
                return verificar
            x += 1
        return verificar

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