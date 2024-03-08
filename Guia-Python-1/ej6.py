
vocales:list = ["a","e","i","o","u"]
def Vocales(frase:str, vocales:list):
    contadorVoc:int = 0
    for i in frase:
        if(i in vocales):
            contadorVoc = contadorVoc+1
        
    return contadorVoc


frase:str = str(input("ingrese una frase para contar la cantidadde vocales que tiene: \n>>"))
print(f"la frase tiene {Vocales(frase, vocales)} vocales")