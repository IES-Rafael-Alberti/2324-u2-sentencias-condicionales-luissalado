def almacenar(contrasena_usuario):
    contrasena ='contraseña'
    if contrasena == contrasena_usuario.lower():
        return True
    else:
        return  False
    
if __name__ == "__main__":
    contrasena_usuario=input("Escriba una contraseña: ")
    if almacenar(contrasena_usuario):
        print("Es correcto")
    else:
        print("Error")


