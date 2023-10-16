def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
    
if __name__=="__main__":
    edad = int(input("¿Cuantos años tienes? "))
    if mayor(edad):
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
    