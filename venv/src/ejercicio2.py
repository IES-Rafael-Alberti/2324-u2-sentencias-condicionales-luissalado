def almacenar(contrasena_usuario):
    contrasena ='contraseña'
    if contrasena == contrasena_usuario.lower():
        return "ES correcta"
    else:
        return  "Es incorrecta"
    
if __name__ == "__main__":
    contrasena_usuario=input("Escriba una contraseña: ")
    print(almacenar(contrasena_usuario))


