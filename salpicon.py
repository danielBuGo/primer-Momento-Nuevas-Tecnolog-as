frutas = []
idFruta = 1
respuesta = int(input("ingresar 1.Si 2. No: "))
while respuesta != 2:
    print("+++++++SALPICONAZO++++++++++++")
    print("1. Registrar Frutas para el salpicon. ")
    print("2. Costo total de su salpicon: ")
    print("3. Mostrar frutas ordenadas de Mayor a menor: ")
    print("4. La fruta mas barata es: ")
    print("5. Salir")
    print("++++++++++++++++++++++++++++++++++")

    opcion = int(input('Digita una opcion: '))
    if opcion == 1:
        fruta = {}
        fruta['id'] = idFruta
        print(f"Fruta ingresada con el id : {idFruta}")
        idFruta += 1
        fruta['nombre'] = input(f"Ingrese el nombre de la fruta: ")
        fruta['precioUnitario'] = float(input(f"Ingrese el precio unitario: "))
        fruta['cantidad'] = int(input(f"Ingrese la cantidad de Fruta: "))
        frutas.append(fruta)
        
    elif opcion == 2:
        costoTotal = 0 
        for fruta in frutas:
          costoTotal += fruta['precioUnitario'] * fruta['cantidad']
          print(f"El costo total de tu salpicón es de {costoTotal}")
          
    elif opcion == 3:
        frutas = sorted(frutas, key=lambda x: x['precioUnitario'], reverse=True)
        for fruta in frutas:
         print(fruta) 
    elif opcion == 4:
         print("FRUTA MÁS BARATA")
         masEconomica = min(frutas, key=lambda x: x['precioUnitario'])
         print(f"Nombre: {masEconomica['nombre']}, Precio Unitario: {masEconomica['precioUnitario']}")     
    else:
        print("Gracias por visitarnos") 
else:
    print("vuelvas pronto")            