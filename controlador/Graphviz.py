from graphviz import Digraph

class Graphviz():
    lista_graph = []

    def implementacion_mapa(self,lista_ruta,lista_estacion):
        f = Digraph(format='png', name='Reporte_Ruta')
        f.attr(rankdir='LR', size='8,5')    # PARA QUE SEA HORIZONTAL
        f.attr('node', shape='circle')

        for linea in lista_estacion:
            
            if (self._estacion_(lista_estacion,linea.getNombre())==True):
                #print('3')
                #f.attr('node', shape='circle')
                f.node(f'{linea.getNombre()}\n{linea.getEstado()}', style='filled',fillcolor=f'{linea.getColor()}')

                

        for linea in lista_ruta:
            if (self._estacion_(lista_estacion,linea.getInicio())==True):
                if (self._estacion_(lista_estacion,linea.getFin())==True):
                    
                    print(self.verificar_estacion(lista_estacion,linea.getInicio()))
                    f.edge(f'{self.verificar_estacion(lista_estacion,linea.getInicio())}', f'{self.verificar_estacion(lista_estacion,linea.getFin())}', label=f'{linea.getNombre()}\n{linea.getPeso()}') 



        f.view()

    def implementacion_ruta(self):
        pass


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