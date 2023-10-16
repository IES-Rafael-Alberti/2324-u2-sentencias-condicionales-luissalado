def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    num = int(input("Escriba un numero: "))
    if par_impar(num):
        print("Es par")
    else:
        print("Es impar")
        
    