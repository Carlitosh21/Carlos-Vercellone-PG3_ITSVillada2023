def bisiesto(year):
    if(year%4 == 0  or year%400==0):
        print(f"{year} es bisiesto")
    else:
        print(f"{year} no es bisiesto")
        
    



year:int = int(input("Ingrese un anio y te dire si es bisiesto o no \n>>"))

bisiesto(year)