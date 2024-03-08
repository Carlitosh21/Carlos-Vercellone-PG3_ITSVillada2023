opcion:int = int(input("Ingrese 1 para imprimir un cuadrado o 2 para imprimir un triángulo: \n>>"))

if opcion == 1:
    ancho:int = int(input("Ingrese el ancho de su cuadrado: \n>>"))
    alto:int = int(input("Ingrese el alto de su cuadrado: \n>>"))
    caracter:str = str(input("Ingrese el caracter de a utilizar: \n>>"))

    for i in range(alto):
        print(ancho*caracter)
elif opcion == 2:
    altura:int = int(input("Ingrese la altura del triángulo: \n>>"))
    caracter:str = str(input("Ingrese el caracter de a utilizar: \n>>"))

    for i in range(1, altura + 1):
        print(caracter * i)

    for i in range(altura - 1, 0, -1):
        print(caracter * i)
else:
    print("Opción no válida. Por favor ingrese 1 o 2.")
