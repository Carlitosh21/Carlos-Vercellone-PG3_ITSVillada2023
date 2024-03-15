class Operaciones:
    n1: int
    n2: int

    def __init__(self):
        print("______________________________________________\n"
              "INGRESE SUS NUMEROS PARA MOSTRARLE EL RESULTADO EN VARIAS OPERACIONES\n"
              "______________________________________________")
        self.n1 = int(input("Ingresa el primer numero: "))
        self.n2 = int(input("Ingrese el segundo numero:"))
        print("______________________________________________")
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
        print("______________________________________________")


    def suma(self):
        resultado_suma:int = self.n1 + self.n2
        print(f"El resultado de la suma es: {resultado_suma}")

    def resta(self):
        resultado_resta1:int = self.n1 - self.n2
        resultado_resta2:int = self.n2 - self.n1

        print(f"El resultado de n1 - n2 es: {resultado_resta1} \nEL resultado de n2 - n1 es: {resultado_resta2}")

    def multiplicacion(self):
        resultado_mult: int = self.n1 * self.n2
        print(f"El resultado de la multiplicacion es: {resultado_mult}")

    def division(self):

        if self.n2 == 0:
            print("El resultado de la division es: ERROR: No se puede dividir por 0")
        else:
            resultado_div: int = self.n1 / self.n2
            print(f"El resultado de la division es: {resultado_div}")

Operaciones()