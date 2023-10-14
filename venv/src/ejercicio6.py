def alumnos(nombre,sexo):
    if sexo == "mujer" and nombre[:1].lower() <= "m":
        return "Eres del grupo A"
    elif sexo == "hombre" and nombre[:1].lower() >= "n":
        return "Eres del grupo A"
    else:
        return "Eres del grupo B"
    
if __name__ == "__main__":
    nombre = input("Escribe tu nombre: ")
    sexo = input ("escribe tu sexo (hombre o mujer): ")
    print(alumnos(nombre,sexo))
     
    