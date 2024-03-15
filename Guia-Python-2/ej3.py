class Triangulo:

    def __init__(self):
        self.lado1 = int(input("Ingresa el primer lado: "))
        self.lado2 = int(input("Ingresa el segundo lado: "))
        self.lado3 = int(input("Ingresa el tercer lado: "))
        self.valor_mayor()
        self.is_equilatero()

    def valor_mayor(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print(f"Todos los lados son iguales ({self.lado1, self.lado2, self.lado3})")
        elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"El lado 1 es el mayor ({self.lado1})")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f"El lado 2 es el mayor ({self.lado2})")
        else:
            print(f"El lado 3 es el mayor ({self.lado3})")

    def is_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es equilatero")
            print("____________________________________________")
        else:
            print("No es equilatero")
            print("____________________________________________")

Triangulo()

    