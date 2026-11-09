inventario = []
def menu():
    print("""
    ===============MENÚ=================
    1. Agregar producto
    2. Agregar lote de productos
    3. Eliminar producto del inventario
    4. Eliminar el producto más reciente
    5. Ordenar productos alfabéticamente
    6. Mostrar número total de productos
    7. Salir
    =====================================
    """)

while True:
    menu()
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("\tOpción no válida")
        continue
    match opcion:
        case 1:
            try:
                print("\tAgregar Prodcuto")
                producto = input("Inserte el nombre de producto: ").capitalize()
                lotedePro = int(input("Inserte el lote de producto: "))
                cantidad = int(input("Agregue la cantidad del producto: "))
                inventario.append([producto,lotedePro,cantidad])
                print("\tProducto agregado correctamente")
            except ValueError:
                print("\tError en el ingreso de un dato\n \tVuelva a intentarlo")
        case 2:
            try:
                print("\tAgregar Lote de Productos")
                cantidadL = int(input("Ingrese la cantidad de lotes a agregar: "))
                for fila in range(cantidadL):
                    nombrepL = input("Ingrese el nombre del producto: ").capitalize()
                    productoL = int(input("Inserte el lote de producto: "))
                    cantidadLo = int(input(f"Inserte la cantidad del lote {fila +1} de producto: "))
                    inventario.append([nombrepL,productoL,cantidadLo])
                print("\tLote agregado correctamente")
            except ValueError:
                print("\tError en el ingreso de un dato\n \tVuelva a intentarlo")
        case 3:
            print("\tEliminar producto del inventario")
            encontrado = False
            nombrePLRm = input("Ingrese el nombre del producto a eliminar: ").capitalize()
            for fila in inventario:
                if fila[0] == nombrePLRm:
                    inventario.remove(fila)
                    encontrado = True
            if encontrado == True:
                print("\tEl prodcuto ha sido eliminado satisfactoriamente")
            else:
                print("\tEl nombre no coincide con el inventario actual")
        case 4:
            print("Eliminar el producto más reciente")
            try:
                inventario.pop()
                print("El producto se ha eliminado correctamente")
            except IndexError:
                print("No hay información para borrar en el momento")
            
        case 5:
            print("Ordenar los productos alfábeticamente")
            inventario.sort()
            print("Los productos se han ordenado satisfactoriamente")
        case 6:
            print("\tMostrar total de productos")
            existencias = 0
            for exis in inventario:
                existencias += exis[-1]
            print(inventario)
            print("Las existencias actuales de todos los productos son : ",existencias)
            print("El inventario de productos es ",len(inventario))
        case 7:
            print("\tHa salido del programa")
            break
        case _:
            print("\tOpción no coincide con ninguna del menú")
        
