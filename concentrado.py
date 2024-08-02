class Concentrado:
    def __init__(self, nombre:str, precio:float, numCalorias:int, registroInvima:str):
        self.__nombre = nombre
        self.__precio = precio
        self.__numCalorias = numCalorias
        self.__registroInvima = registroInvima
        
    def dar_nombre(self):
        return self.__nombre
    
    def dar_precio(self):
        return self.__precio
    
    def dar_numCalorias(self):
        return self.__numCalorias
    
    def dar_informacion(self):
        return self.dar_nombre() + ' (' + str(self.dar_precio()) + ').'
    
    def calcular_rentabilidad(self):
        return round(self.dar_precio / self.dar_numCalorias, 2)