from animal_exotico import AnimalExotico

class Huron(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        
    def hacer_sonido(self):
        return 'Eek eek'
    
    