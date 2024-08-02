from animal_exotico import AnimalExotico

class Boa_Constrictor(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0
        
    def hacer_sonido(self):
        return('¡Tsss!')
    
    def comer_ratones(self, ratones: int) -> None:
        self.__ratones_comidos += ratones
    
    def obtener_ratones_comidos(self) -> int:
        return self.__ratones_comidos
    
    