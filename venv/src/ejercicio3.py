def division(X,Y):
    if X == 0:
        return "Error"
    else:
        resultado = Y / X
        return resultado
    
if __name__ == "__main__":
    
    Y = int(input("Pon un numero: "))
    X = int(input("Pon un numero: "))
    print(division(X,Y))