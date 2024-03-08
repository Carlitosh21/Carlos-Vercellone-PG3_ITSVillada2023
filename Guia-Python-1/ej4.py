lista:list = [3,9,5,10,77,34,12,0,1,79]

print(f"lista originial: {lista}")

def Acomodar(lista:list):
    lista.sort(reverse=False)
    return lista


lista_Acomodada: list = print(f"lista cambiada: {Acomodar(lista)}")