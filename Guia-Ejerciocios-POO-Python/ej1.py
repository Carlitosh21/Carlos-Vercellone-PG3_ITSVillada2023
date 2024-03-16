class Persona:

    def inicializar(self,name):
        self.nombre= name 

    def imprimir(self):
        print("Nombre de la persona: ",self.nombre)



persona1 = Persona()
persona1.inicializar("Juan")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Kevin")
persona2.imprimir()