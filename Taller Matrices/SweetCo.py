matVentas = [
    [100,88,92,94,85,110,118],
    [30,42,31,32,38,40,37],
    [23,35,39,45,55,60,61],
    [45,50,56,65,47,57,68],
    [18,25,33,21,22,28,32]
]

lstPrecios = [1500,5000,6500,2500,22500]

#1. Producto que genera más ingresos en la semana

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

lstTotales = lstTotalesProdXSem(matVentas,lstPrecios)

maxTotal = max(lstTotales)
prodVentMax = lstTotales.index(maxTotal) + 1

print(f"El producto {prodVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")

#2. Día de la semana con mayor ingresos