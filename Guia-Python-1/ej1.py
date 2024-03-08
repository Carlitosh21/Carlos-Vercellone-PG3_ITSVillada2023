def find_index(valor, lista):
    if valor in lista:
        return lista.index(valor)
    else:
        return -1 

lista = [8, 12, 9, 45]
valor = int(input("Ingrese un valor para buscar dentro de la lista " + str(lista) + ":\n"))
indice = find_index(valor, lista)

if indice != -1:
    print(f"El índice del valor {valor} es: {indice}")
else:
    print("El valor no fue encontrado en la lista.")
