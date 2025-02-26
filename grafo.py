from collections import deque
import heapq

class Grafo:
    def __init__(self, lista_adyacencia):
        self.lista_adyacencia = lista_adyacencia

    # Devuelve los vecinos de un nodo en la lista de adyacencia.
    def obtener_vecinos(self, v):
        return self.lista_adyacencia.get(v, [])
    
    # Calcula la heurística usando la distancia Manhattan.
    def h(self, nodo, destino):
        return abs(nodo[0] - destino[0]) + abs(nodo[1] - destino[1])
    
    # Implementa la búsqueda en profundidad (DFS) para encontrar un camino en el grafo.
    def primero_profundidad(self, nodo_inicio, nodo_final):
        visitados = set()
        return self._dfs(nodo_inicio, nodo_final, visitados, [])
    
    # Función auxiliar recursiva para realizar DFS.
    def _dfs(self, actual, destino, visitados, camino):
        if actual in visitados:
            return None
        
        visitados.add(actual)
        camino.append(actual)

        if actual == destino:
            return list(camino)

        for vecino in self.obtener_vecinos(actual):
            resultado = self._dfs(vecino, destino, visitados, camino)
            if resultado:
                return resultado

        camino.pop()
        return None
    
    # Implementa la búsqueda en anchura (BFS) para encontrar un camino en el grafo.
    def primero_anchura(self, nodo_inicio, nodo_final):
        visitados = set()
        cola = deque([(nodo_inicio, [nodo_inicio])])
        
        while cola:
            actual, camino = cola.popleft()
            if actual == nodo_final:
                return camino
            
            if actual not in visitados:
                visitados.add(actual)
                for vecino in self.obtener_vecinos(actual):
                    if vecino not in visitados:
                        cola.append((vecino, camino + [vecino]))
        
        return None
    
    # Implementa el algoritmo A* para encontrar el camino óptimo combinando costo real y heurística.
    def a_estrella(self, nodo_inicio, nodo_final):
        open_set = []
        heapq.heappush(open_set, (0, nodo_inicio))
        came_from = {}
        g_score = {nodo: float('inf') for nodo in self.lista_adyacencia}
        g_score[nodo_inicio] = 0
        f_score = {nodo: float('inf') for nodo in self.lista_adyacencia}
        f_score[nodo_inicio] = self.h(nodo_inicio, nodo_final)
        
        while open_set:
            _, actual = heapq.heappop(open_set)
            
            if actual == nodo_final:
                camino = []
                while actual in came_from:
                    camino.append(actual)
                    actual = came_from[actual]
                camino.append(nodo_inicio)
                return camino[::-1]
            
            for vecino in self.obtener_vecinos(actual):
                tentative_g_score = g_score[actual] + 1
                if tentative_g_score < g_score[vecino]:
                    came_from[vecino] = actual
                    g_score[vecino] = tentative_g_score
                    f_score[vecino] = tentative_g_score + self.h(vecino, nodo_final)
                    heapq.heappush(open_set, (f_score[vecino], vecino))
        
        return None