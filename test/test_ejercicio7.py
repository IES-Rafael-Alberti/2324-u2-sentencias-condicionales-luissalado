from src.ejercicio7 import renta


def test_renta():
    cantidad = 78
    assert renta(cantidad) == "5%"