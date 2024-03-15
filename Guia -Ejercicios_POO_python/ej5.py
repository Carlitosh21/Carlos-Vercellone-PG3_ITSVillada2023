class Persona:

    def __init__(self, nom:str, edad:int):
        self.name:str = nom
        self.age:int = edad

    def imprimir(self):
        print("___________________________\n    PERSONA")
        print("___________________________")
        print("Nombre: ",self.name)
        print("Edad: ",self.age)
        print("___________________________")

class Empleado(Persona):

    def __init__(self, nom:str, edad:int, suel:int):
        super().__init__(nom,edad)
        self.sueldo:int = suel

    def imprimir(self):
        print("___________________________\n    EMPLEADO")
        print("___________________________")
        print("Nombre: ",self.name)
        print("Edad: ",self.age)
        print("Sueldo: ",self.sueldo)
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
        print("___________________________")


# Bloque Principal
        
persona1 = Persona("Valentina", 16)
persona1.imprimir()
empleado1 = Empleado("Carlos", 17, 4000)
empleado1.imprimir()
empleado2 = Empleado("Gustavo", 28, 1890)
empleado2.imprimir()