class Alumno:

    def __init__(self, name:str, mark:int):
        self.nombre = name
        self.nota = mark
        self.imprimir()
        self.mostrar_nota()

    def imprimir(self):

        print(f"Alumno: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_nota(self):
        if self.nota >= 4:
            print("Estado: Regular")
            print("____________________________________________")
        else:
            print("Estado: Libre")
            print("____________________________________________")


Alumno1 = Alumno("Joaquin", 7)
Alumno2 = Alumno("Federico", 3)