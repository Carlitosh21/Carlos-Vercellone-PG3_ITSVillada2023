print("SUMA DE NUMEROS")

n1:int = int(input("Ingresa el primer numero: "))
n2:int = int(input("Ingresa el segundo numero: "))
suma:int = n1 + n2
print("La suma es: ", suma)

opcion:str = str(input("Desea seguir sumando numeros? s/n\n>> "))
if opcion == "s":
    a = True
elif opcion =="n":
    a = False
else:
    print("Opcion no valida, CERRANDO EL PROGRAMA")
    a = False

while a == True: 
    
    
    try:
        n:int = int(input("Ingrese el siguiente numero: "))
        n/1
        suma:int = suma+n
    except ValueError:
        
        print("El caracter ingresado no es numerico")
        break



print("El resultado es: ", suma)
        
    


    