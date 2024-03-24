articulos = []
idProducto = 1
zonas = {
    'A': {'espacio': 0, 'articulos': []},
    'B': {'espacio': 0, 'articulos': []},
    'C': {'espacio': 0, 'articulos': []},
    'D': {'espacio': 0, 'articulos': []}
}

respuesta = int(input("Desea ingresar al menú: 1.Si 2. No: "))

while respuesta != 2:
    print("+++++++Menú Comic Shop++++++++++++")
    print("1. Registrar producto")
    print("2. Mostrar los productos de la bodega: ")
    print("3. Mostrar Id, nombre, precio unitario y descripcion: ")
    print("4. Modificar unidades compradas: ")
    print("5. Salir")
    print("++++++++++++++++++++++++++++++++++")

    opcion = int(input('Digita una opcion: '))

    if opcion == 1:
        articulo = {}
        zona = {} 
        articulo['id'] = idProducto        
        print(f"Articulo ingresado con el id : {idProducto}")
        idProducto += 1
        articulo['nombre'] = input("Ingrese el nombre del producto: ")
        articulo['precio'] = int(input("Cual es el precio unitario?: "))     
                 
        ubicacion = input("Ingrese la zona de ubicacion en la tienda (A, B, C o D): ").upper()
        while ubicacion not in zonas:
          print("La ubicación ingresada no es válida. Por favor, ingrese una de las opciones: A, B, C o D.")
          ubicacion = input("Ingrese la zona de ubicacion en la tienda (A, B, C o D): ").upper()

        zona['ubicacion'] = ubicacion
                 
        cantidad = int(input("Cuantos va a llevar?: "))
        while cantidad < 0:
            print("Debes ingresar una cantidad válida.")
            cantidad = int(input("Cuantos va a llevar?: "))        
        if cantidad <= 50:
            zonas[ubicacion]['cantidad'] = cantidad
        else:
            print("No puedes llevar más de 50 artículos en una misma zona")
            continue
        articulo['cantidad'] = cantidad     
        articulo['Zona'] = zona 
        articulo['descripcion'] = input("Ingrese una breve descripcion del producto: ")
        articulo['fabricante'] = input("Ingrese el fabricante del prodcuto: ")
        articulo['alfanumerico'] = int(input("Agregue codigo Alfanumerico: "))                   
        articulo['pais'] = input("Pais de fabricacion: ")
        articulo['garantia'] = input("El producto tiene garantía? (Sí/No): ").lower() == "sí"
        articulos.append(articulo) 
                      
    elif opcion == 2:
      for articulo in articulos:
        print(articulo)                             
         
    elif opcion == 3:
      buscarProducto = input("Ingrese el nombre del producto que desea buscar: ")
      encontrado = False
      for articulo in articulos:
        if articulo['nombre'].lower() == buscarProducto.lower():
          encontrado = True
          print("Información del producto encontrado:")
          print(f"ID: {articulo['id']}")
          print(f"Nombre: {articulo['nombre']}")
          print(f"Precio unitario: {articulo['precio']}")
          print(f"Descripción: {articulo['descripcion']}")
          break
      if not encontrado:
        print(f"No se encontró ningún producto con el nombre '{buscarProducto}'.")
          
    elif opcion == 4:
      modificarArticulo = int(input("Ingrese el ID del producto que desea modificar: "))
      nuevaCantidad = int(input("Ingrese la nueva cantidad de unidades compradas: "))
      encontrado = False
      for articulo in articulos:
        if articulo['id'] == modificarArticulo:
          encontrado = True
          if nuevaCantidad <= 50:
            ubicacionZona = articulo['Zona']['ubicacion']
            zonas[ubicacionZona]['cantidad'] -= articulo['cantidad']
            articulo['Zona']['cantidad'] = nuevaCantidad
            zonas[ubicacionZona]['cantidad'] += nuevaCantidad
            print(f"Se ha modificado la cantidad de unidades del producto '{articulo['nombre']}' a {nuevaCantidad}.")
          else:
            print("No puedes llevar más de 50 artículos en una misma zona")
            break
      if not encontrado:
        print(f"No se encontró ningún producto con el ID '{modificarArticulo}'.")                 
               
    else:
      print("Saliste del menú")
      
else:
  print("Fin")