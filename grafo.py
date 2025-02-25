def leer_laberinto(archivo):
    """
    Lee el archivo de laberinto y devuelve:
    - dimensiones: tupla (N, M) con las dimensiones del laberinto.
    - laberinto: lista de listas (matriz) con los valores leídos.
    """
    with open(archivo, "r") as file:
        lineas = file.readlines()

    # Primera línea: algo como (17,17) o similar.
    # Retiramos paréntesis, salto de línea y separamos por coma.
    dimensiones = tuple(map(int, lineas[0].strip("()\n").split(",")))

    # El resto de líneas son filas del laberinto
    laberinto = []
    for linea in lineas[1:]:
        # Ejemplo de línea: [2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, ...]
        # Quitamos corchetes, saltos de línea, espacios y convertimos a int.
        fila = list(map(int, linea.strip("[]\n ").split(",")))
        laberinto.append(fila)

    return dimensiones, laberinto

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
        #inserte si codigo aqui
        return None
    
    def a_estrella(self, nodo_inicio, nodo_final):
        #inserte si codigo aqui
        return None