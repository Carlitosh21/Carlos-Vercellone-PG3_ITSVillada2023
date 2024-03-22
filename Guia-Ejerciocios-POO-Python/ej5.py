class Persona:

    def __init__(self):
        self.name:str = input("Nombre: ")
        self.age:int = input("Edad: ")

    def imprimir(self):
        print("___________________________\n    PERSONA")
        print("___________________________")
        print("Nombre: ",self.name)
        print("Edad: ",self.age)
        print("___________________________")

class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo:int = int(input("Sueldo: "))

    def imprimir(self):
        print("___________________________\n    EMPLEADO")
        print("___________________________")
        print("Nombre: ",self.name)
        print("Edad: ",self.age)
        print("Sueldo: ",self.sueldo)
        if self.sueldo >= 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
        print("___________________________")


# Bloque Principal

persona1 = Persona()
persona1.imprimir()
Empleado1 = Empleado()
Empleado1.imprimir()