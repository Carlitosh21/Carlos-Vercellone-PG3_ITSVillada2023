

def esCapicua(word:str):
    word = word.lower()
    if(word == word[::-1]):
        print(f"{word} es capicua")
    else:
        print(f"{word} NO es capicua")
    
word:str = str(input("Escriba una palabra para analizar si es o no un palíndromo: \n>>"))
esCapicua(word)