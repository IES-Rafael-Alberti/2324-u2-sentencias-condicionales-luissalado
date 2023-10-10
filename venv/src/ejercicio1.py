def mayor(edad):
    if edad >= 18:
        return f"Eres mayor de edad"
    else:
        return f"Eres menor de edad"
    
if __name__=="__main__":
    edad = int(input("¿Cuantos años tienes? "))
    print(mayor(edad))