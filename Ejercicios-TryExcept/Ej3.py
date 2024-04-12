mes = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

try:
    num_mes:int = int(input("Ingresa el mes (1-12): "))
    print(mes[num_mes-1])
except IndexError:
    print("El mes no existe, Index fuera de rango, por favor ingresar un numero entre 1 y 12")
    