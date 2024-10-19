class Disciplina:
    
    def __init__(self,nombre:str):
        self.__nombre = nombre
        self.__cantParticipantes = []
        
    
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre de la disciplina debe ser un string.")
        self.__nombre = nombre
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def agregarParticipante(self,participante:"Participante"):
        self.__cantParticipantes.append(participante)
        
    def __str__(self):
        return f"Disciplina: {self.__nombre}\nParticipantes: {', '.join([str(participante) for participante in self.__cantParticipantes])}"