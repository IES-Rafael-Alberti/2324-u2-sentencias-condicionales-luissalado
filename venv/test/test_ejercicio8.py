from src.ejercicio8 import puntuacion


def test_puntuacion():
    puntos = 0.4
    assert puntuacion(puntos) == "Su puntuacion es 0.4 y cantidad de dinero es 960.0"