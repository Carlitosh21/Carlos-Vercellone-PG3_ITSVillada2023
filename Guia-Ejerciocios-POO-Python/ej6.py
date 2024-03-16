class Familia:
    def __init__(self, nombreP:str, nombreM:str, hijos:list):

        self.Padre:str = nombreP
        self.Madre:str = nombreM
        self.hijos:list = hijos

    def __str__(self):
        return f"Padre: {self.Padre}\nMadre: {self.Madre}\nHijos: {self.hijos}"
    

Familia1 = Familia("Pedro","Maria",["Juan", "Valentino", "Paula"])
print(Familia1)