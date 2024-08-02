class Gato:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
    
    def maullar(self):
        return 'miau!'