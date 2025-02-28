def graficar_ruta(ruta, tamaño):
    matriz = [["." for _ in range(tamaño)] for _ in range(tamaño)]

    for x, y in ruta:
        matriz[x][y] = "█"  # Notar que y es la fila y x es la columna

    for fila in matriz:
        print(" ".join(fila))