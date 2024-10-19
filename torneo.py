
class Torneo:
    
    def __init__(self,nombre:str,ubicacion:str):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__participantes=[]
        self.__disciplinas = []
           
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre del torneo debe ser una cadena de caracteres.")
        self.__nombre = nombre
        
    def obtenerNombre(self)->str:
        return self.__nombre
        
    
    def establecerUbicacion(self,ubicacion:str):
        if not isinstance(ubicacion,str):
            raise ValueError("la ubi del torneo debe ser una cadena de caracteres.")
        self.__ubicacion = ubicacion
    
    def obtenerUbicacion(self)->str:
        return self.__ubicacion
    
    
    def agregarParticipante(self,Participante):
        self.__participantes.append(Participante)
        
    def agregarDisciplina(self,Disciplina):
        self.__disciplinas.append(Disciplina)
        
    def __str__(self)->str:
        return f"Torneo: {self.__nombre}, Ubicacion: {self.__ubicacion}, Participantes: {self.__participantes}, Disciplinas: {self.__disciplinas}"
        