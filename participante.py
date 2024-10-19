class Participante:
    
    def __init__(self,nombre:str,edad:int,nacionalidad:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplina=[]
        
        
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("debe ser un nombre")
        self.__nombre = nombre
        
        
    def establecerEdad(self,edad:str):
        if not isinstance(edad,str):
            raise ValueError("la edad debe ser un entero")
        self.__edad = edad
        
        
    def establecerNacionalidad(self,nacionalidad:str):
        if not isinstance(nacionalidad,str):
            raise ValueError("la nacionalidad debe ser valida")
        self.__nacionalidad = nacionalidad
        
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerNacionalidad(self)->str:
        return self.__nacionalidad
    
    def agregaraDisciplina(self,disciplina):
        self.__disciplina.append(disciplina)
    
    def obtenerDisciplinas(self):
        return self.__disciplina
    
    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Nacionalidad: {self.__nacionalidad}"