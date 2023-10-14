def tributo_edad(Cantidad,edad):
    if edad >=16 and Cantidad >= 1000:
        return True
    else:
        return False
    
if __name__ == "__main__":
    edad = int(input("¿Cuantos años tienes?: "))
    cantidad = float(input("¿Cuales son sus ingresos mensuales?: "))
    if tributo_edad(cantidad,edad):
        print("Tienes q tributar")
    else:
        print("No tienes que tributar")
    
