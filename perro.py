from concentrado import Concentrado
class Perro:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int, concentradoPreferencia: Concentrado):
        self.__nombre = nombre
        self.__raza = raza
        self.__peso = peso
        self.__edad = edad
        self.__concentradoPreferencia = concentradoPreferencia
    
    def ladrar(self):
        return 'Guau, guau'
    
    def modificar_peso(self, nuevo_peso: float):
        self.__peso = nuevo_peso
        
    def dar_nombre(self):
        return self.__nombre
    
    def dar_concentrado(self):
        return self.__concentradoPreferencia.dar_nombre()
    
    def dar_informacion(self):
        return self.__nombre + ' (' + self.__raza + '): ' + str(self.__peso) + ' / ' + str(self.__edad)