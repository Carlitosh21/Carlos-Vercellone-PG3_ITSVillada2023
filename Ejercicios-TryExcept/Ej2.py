

n1:int = int(input("Ingresa el primer numero: "))
n2:int = int(input("Ingresa el segundo numero: "))

try:
    print("La division es: ", n1/n2)
except ZeroDivisionError:
    print("No se puede dividir por 0")