def crearMatriz(fils,cols, valor = 0):
    mat = []
    for f in range(fils):
        mat.append([valor] * cols)
    return mat

def llenarMatriz(matriz):
    fils = len(matriz)
    cols = len(matriz[0])
    for f in range(fils): 
        for c in range(cols): 
            matriz[f][c] = input("Ingrese datos: ")

def imprimirMatriz(matriz):
    fils = len(matriz)
    cols = len(matriz[0])
    for f in range(fils): 
        for c in range(cols): 
            print(matriz[f][c], end="\t") 
        print("") 

filas = int(input("Cantidad de filas: "))
columnas = int(input("Cantidad de columnas: "))
matriz = crearMatriz(filas,columnas)
llenarMatriz(matriz)
imprimirMatriz(matriz)

