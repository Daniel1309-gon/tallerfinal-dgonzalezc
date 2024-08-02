from concentrado import Concentrado

class Guarderia:
    def __init__(self, nombre: str, ubicacion: str, concentrados: list[Concentrado]) -> None:
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__concentrados = concentrados
        
    def dar_nombre(self):
        return self.__nombre
    
    def dar_ubicacion(self):
        return self.__ubicacion
    
    def dar_concentrados(self):
        return self.__concentrados