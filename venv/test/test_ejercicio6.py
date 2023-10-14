from src.ejercicio6 import alumnos

def test_alumnos():
    nombre = "andrea"
    sexo = "mujer"
    assert alumnos(nombre,sexo) == "Eres del grupo A"