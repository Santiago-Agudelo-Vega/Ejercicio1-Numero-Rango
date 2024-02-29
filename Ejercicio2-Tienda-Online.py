#Elaborar un programa que tenga 4 articulos y determinar cuantos se han comprado, precio constante, total de suma de los articulos, 
#Cuantos de cada uno, 2 Opciones Cancelar, facturar
# Constantes para los precios de los productos
PRECIO_COMPUTADORA = 1000
PRECIO_TABLETA = 500
PRECIO_PROYECTOR = 800
PRECIO_TELEVISION = 1200

# Inicializar variables para contar la cantidad de cada producto
cuenta_computadora = 0
cuenta_tableta = 0
cuenta_proyector = 0
cuenta_television = 0

# Función para calcular y mostrar la factura
def mostrar_factura():
    costo_total_computadora = cuenta_computadora * PRECIO_COMPUTADORA
    costo_total_tableta = cuenta_tableta * PRECIO_TABLETA
    costo_total_proyector = cuenta_proyector * PRECIO_PROYECTOR
    costo_total_television = cuenta_television * PRECIO_TELEVISION
    
    total_articulos = cuenta_computadora + cuenta_tableta + cuenta_proyector + cuenta_television
    total_pago = costo_total_computadora + costo_total_tableta + costo_total_proyector + costo_total_television
    
    print("FACTURA")
    print("-------")
    print(f"Computadoras de escritorio: {cuenta_computadora} - Costo total: ${costo_total_computadora}")
    print(f"Tabletas: {cuenta_tableta} - Costo total: ${costo_total_tableta}")
    print(f"Proyectores: {cuenta_proyector} - Costo total: ${costo_total_proyector}")
    print(f"Televisores: {cuenta_television} - Costo total: ${costo_total_television}")
    print("-------")
    print(f"Total de artículos: {total_articulos}")
    print(f"Total a pagar: ${total_pago}")

# Bucle principal para recibir continuamente productos
while True:
    print("Elige un producto para añadir (1. Computadoras de escritorio, 2. Tabletas, 3. Proyectores, 4. Televisores)")
    eleccion = input("Ingresa tu elección (o escribe 'FACTURA' para mostrar la factura): ").upper()

    if eleccion == '1':
        cuenta_computadora += 1
    elif eleccion == '2':
        cuenta_tableta += 1
    elif eleccion == '3':
        cuenta_proyector += 1
    elif eleccion == '4':
        cuenta_television += 1
    elif eleccion == 'FACTURA':
        mostrar_factura()
        break
    else:
        print("Opción inválida. Por favor, ingresa una opción válida.")

