def puntuacion(puntos):
    if puntos == 0.0:
        total = puntos * 2400
        return f"Su puntuacion es 0.0 y cantidad de dinero es {total}"
    elif puntos == 0.4:
        total = puntos * 2400
        return f"Su puntuacion es 0.4 y cantidad de dinero es {total}"
    else:
        total = puntos * 2400
        return f"Su puntuacion es {puntos} y cantidad de dinero es {total}"
    
if __name__ == "__main__":
    print ("Nivel	Puntuación")
    print ("Inaceptable	0.0")
    print ("Aceptable	0.4")
    print ("Meritorio	0.6 o más")
    puntos = float(input("Cual ha sido su puntuacion: "))
    print(puntuacion(puntos))
        