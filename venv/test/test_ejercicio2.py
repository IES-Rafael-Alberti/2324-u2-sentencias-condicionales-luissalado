from src.ejercicio2 import  almacenar

def test_almacenar():
    contrasena_usuario = "contraseña"
    assert almacenar(contrasena_usuario) == "ES correcta"