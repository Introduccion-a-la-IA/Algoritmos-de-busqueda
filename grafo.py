from collections import deque


class Grafo:

    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    def obtener_vecinos(self, v):
        return self.lista_adyacencia.get(v,[])

    # funcion heuristica
    def h(self, n):
        #inserte su codigo aqui
        return H[n] # puede retornar una lista con el calculo de la heuristica para cada estado
    
    def primero_profundidad(self, nodo_inicio, nodo_final):
        visitados = set()
        return self._dfs(nodo_inicio, nodo_final, visitados, [])
    
    def _dfs(self, actual, destino, visitados, camino):
        if actual in visitados:
            return None
        
        visitados.add(actual)
        camino.append(actual)

        if actual == destino:
            return list(camino)  # Devolver la copia del camino encontrado

        for vecino in self.obtener_vecinos(actual):
            resultado = self._dfs(vecino, destino, visitados, camino)
            if resultado:  
                return resultado  # Retornar el primer camino válido encontrado

        camino.pop()  # Si no encontramos camino, retrocedemos
        return None  # Si no hay solución
        
    def primero_anchura(self, nodo_inicio, nodo_final):
        visitados = set()
        cola = deque([(nodo_inicio, [nodo_inicio])])  # Inicializamos la cola con el nodo inicial
        
        while cola:
            actual, camino = cola.popleft() 
            if actual == nodo_final:
                return camino  # Se encontró un camino
            
            if actual not in visitados:
                visitados.add(actual)
                for vecino in self.obtener_vecinos(actual):
                    if vecino not in visitados:
                        cola.append((vecino, camino + [vecino]))  # Encolamos nuevo camino

        return None  # Si no hay camino
    
    def a_estrella(self, nodo_inicio, nodo_final):
        #inserte si codigo aqui
        return None