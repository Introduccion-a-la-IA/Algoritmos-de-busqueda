from grafo import Grafo
import os
from grafica import graficar_ruta

def encontrar_puntos_especiales(matriz):
    inicio = None
    destino = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 2:
                inicio = (i, j)
            elif matriz[i][j] == 3:
                destino = (i, j)

    return inicio, destino

def leer_matriz_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        archivo.readline()  # Ignorar la primera línea
        
        # Leer el resto del archivo y convertirlo en una matriz
        matriz = []
        for linea in archivo:
            fila = list(map(int, linea.strip().strip("[]").split(",")))
            matriz.append(fila)

    return matriz

def matriz_a_lista_adyacencia(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    lista_adyacencia = {}

    # Movimientos permitidos (arriba, abajo, izquierda, derecha)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] in (0,2,3):  # Solo si es transitable
                nodo_actual = (i, j)
                lista_adyacencia[nodo_actual] = []

                for dx, dy in movimientos:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < filas and 0 <= nj < columnas and matriz[ni][nj] in (0,2,3):
                        lista_adyacencia[nodo_actual].append((ni, nj))

    return lista_adyacencia


if __name__ == "__main__":
    nombre_archivo = os.path.join(os.path.dirname(__file__), "laberinto50.txt")
    matriz = leer_matriz_desde_archivo(nombre_archivo)

    inicio, destino = encontrar_puntos_especiales(matriz)

    lista_adyacencia = matriz_a_lista_adyacencia(matriz)
    print(inicio, destino)
    grafo = Grafo(lista_adyacencia)
    
    rutadfs = grafo.primero_profundidad(inicio, destino)
    if rutadfs:
        print("\nRuta encontrada DFS:", rutadfs)
        graficar_ruta(rutadfs,50)
    
    else:
        print("\nNo se encontró una ruta")
        
    rutabfs = grafo.primero_anchura(inicio, destino)
    if rutabfs:
        print("\nRuta encontrada BFS:", rutabfs)
        graficar_ruta(rutabfs,50)
    else:
        print("\nNo se encontró una ruta")

    ruta_a_estrella = grafo.a_estrella(inicio, destino)
    if ruta_a_estrella:
        print("\nRuta encontrada con A*:", ruta_a_estrella)
        graficar_ruta(ruta_a_estrella,50)
    else:
        print("\nNo se encontró una ruta con A")