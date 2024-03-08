def NumStep(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if abs(int(numero_str[i]) - int(numero_str[i + 1])) != 1:
            return False
    return True
        
        
num: str= (input("Ingrese un numero para saber si es un Step: \n>>"))
if(NumStep(num)):
    print(f"el numero {num} era Step!")
else:
    print(f"el numero {num} NO era Step!")