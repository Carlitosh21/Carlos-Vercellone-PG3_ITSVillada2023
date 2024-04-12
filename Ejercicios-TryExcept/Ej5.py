try:
    with open("ejemplo.txt", "w") as file:
        
        file.write(5)

except TypeError:
    print("Error: Se ha producido un error al intentar escribir un entero en el archivo de texto.")
except Exception as e:
    print("Se ha producido un error:", e)