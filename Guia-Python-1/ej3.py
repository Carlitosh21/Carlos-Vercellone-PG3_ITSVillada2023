ancho:int = int(input("Ingrese el ancho de su cuadrado: \n>>"))
alto:int = int(input("Ingrese el alto de su cuadrado: \n>>"))
caracter:str = str(input("Ingrese el caracter de a utilizar: \n>>"))

for i in range(alto):
    print(ancho*caracter)