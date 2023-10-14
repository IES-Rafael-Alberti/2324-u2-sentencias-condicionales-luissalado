def programa(edad):
    if edad < 4:
        return "Gratis"
    elif edad >= 4 and edad <=18:
        return "La entrada cuesta 5$"
    else:
        return "La entrada cuesta 10$"
    
if __name__ == "__main__":
    edad = int(input("¿Cuantos años tienes? "))
    print(programa(edad))