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
        while True:           
          zona['ubicacion'] = input("Ingrese la zona de ubicacion en la tienda (A, B, C o D): ").upper()
          if zona['ubicacion'] in zonas:         
            
            break
          else:
            print("La ubicación ingresada no es válida. Por favor, ingrese una de las opciones: A, B, C o D.")
                 
        zona['cantidad'] = int(input("Cuantos va a llevar?: "))
        while zona["cantidad"] < 0:
            print("Debes ingresar una cantidad valida.")
            zona['cantidad'] = int(input("Cuantos va a llevar?: "))
        
        if zona["cantidad"] <= 50:
            zonas[zona['ubicacion']]['cantidad'] = zona["cantidad"]
        else:
            print("No puedes llevar más de 50 artículos en una misma zona")
            continue     
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
      modificarArticulo = int(input("Que articulo deseas modificar?: "))
      articuloSeleccionado = None
      for articulo in articulos:
        modificarArticulo = int(input("Ingrese el ID del producto que desea modificar: "))
        nuevaCantidad = int(input("Ingrese la nueva cantidad de unidades compradas: "))
        encontrado = False
        for articulo in articulos:
            if articulo['id'] == modificarArticulo:
                encontrado = True
                if nuevaCantidad <= 50:
                    articulo['Zona']['cantidad'] = nuevaCantidad
                    print(f"Se ha modificado la cantidad de unidades del producto '{articulo['nombre']}' a {nuevaCantidad}.")
                else:
                    print("No puedes llevar más de 50 artículos en una misma zona")
                break
        if not encontrado:
            print(f"No se encontró ningún producto con el ID '{modificarArticulo}'.")
          
        else:
            print('no seleccionaste una vanda valida')                  
               
    else:
      print("Saliste del menú")
      
else:
  print("Fin")
        
        
        

    
