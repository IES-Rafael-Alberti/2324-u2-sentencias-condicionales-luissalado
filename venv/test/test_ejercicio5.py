from src.ejercicio5 import tributo_edad


def test_tributo_edad():
    edad = 18
    cantidad = 1892
    assert tributo_edad(cantidad,edad) == True
    