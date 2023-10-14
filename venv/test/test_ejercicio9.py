from src.ejercicio9 import programa


def test_programa():
    edad = 78
    assert programa(edad) == "La entrada cuesta 10$"