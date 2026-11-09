
lstPrecios = [1500,5000,6500,2500,22500]

#1. Producto que genera más ingresos en la semana

def crearMatriz(fils,cols, valor = 0):
    mat1 = []
    for f in range(fils):
        mat1.append([valor] * cols)
    return mat1

def llenarMatriz(matriz):
    fils = len(matriz)
    cols = len(matriz[0])
    for f in range(fils): 
        for c in range(cols): 
            matriz[f][c] = int(input("Ingrese datos: "))

def imprimirMatriz(matriz):
    fils = len(matriz)
    cols = len(matriz[0])
    for f in range(fils): 
        for c in range(cols): 
            print(matriz[f][c], end="\t") 
        print("") 

def lstTotalesProdXSem(ventas,precios):
    filas = len(ventas)
    cols = len(ventas[0])
    lstTotales = []
    for f in range(filas):
        suma = 0
        for c in range(cols):
            suma += ventas[f][c] * precios[f]
        lstTotales.append(suma)

    return lstTotales

filas = int(input("Cantidad de filas: "))
columnas = int(input("Cantidad de columnas: "))
matVentas = crearMatriz(filas,columnas)
llenarMatriz(matVentas)
imprimirMatriz(matVentas)

lstTotales = lstTotalesProdXSem(matVentas,lstPrecios)

maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal) + 1

print(f"El producto {prodVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")

#2. Día de la semana con mayor ingresos