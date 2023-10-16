def renta(cantidad):
    if cantidad < 10000:
        return "5%"
    elif cantidad >= 10000 and cantidad <= 20000:
        return "15%"
    elif cantidad >= 20000 and cantidad <= 35000:
        return "20%"
    elif cantidad >= 35000 and cantidad <= 60000:
        return "30%"
    else:
        return "45%"
    
if __name__ == "__main__":
    cantidad = int(input("¿Cuanto cobras?: "))
    print(renta(cantidad))