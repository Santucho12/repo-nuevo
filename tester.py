from torneo import Torneo
from disciplina import Disciplina
from participante import Participante

class Tester:
    
    def __init__(self):
        self.torneo = None

    def crear_torneo(self):
        nombre = input("Ingrese el nombre del torneo: ")
        ubicacion = input("Ingrese la ubicación del torneo: ")
        self.torneo = Torneo(nombre, ubicacion)
        print(f"Torneo '{nombre}' creado en {ubicacion}.")

    def agregar_disciplina(self):
        nombre_disciplina = input("Ingrese el nombre de la disciplina: ")
        disciplina = Disciplina(nombre_disciplina)
        self.torneo.agregarDisciplina(disciplina)
        print(f"Disciplina '{nombre_disciplina}' agregada al torneo.")

    def agregar_participante(self):
        nombre_participante = input("Ingrese el nombre del participante: ")
        edad = int(input("Ingrese la edad del participante: "))
        nacionalidad = input("Ingrese la nacionalidad del participante: ")
        participante = Participante(nombre_participante, edad, nacionalidad)
        self.torneo.agregarParticipante(participante)
        print(f"Participante '{nombre_participante}' agregado al torneo.")

    def inscribir_participante(self):
        nombre_participante = input("Ingrese el nombre del participante para inscribir: ")
        nombre_disciplina = input("Ingrese el nombre de la disciplina: ")

        participante = next((p for p in self.torneo._Torneo__participantes if p.obtenerNombre() == nombre_participante), None)
        disciplina = next((d for d in self.torneo._Torneo__disciplinas if d.obtenerNombre() == nombre_disciplina), None)

        if participante and disciplina:
            participante.agregaraDisciplina(disciplina)
            disciplina.agregarParticipante(participante)
            print(f"{participante.obtenerNombre()} ha sido inscrito en la disciplina {disciplina.obtenerNombre()}.")
        else:
            print("Participante o disciplina no encontrados.")

    def mostrar_participantes_por_disciplina(self):
        nombre_disciplina = input("Ingrese el nombre de la disciplina para ver participantes: ")
        disciplina = next((d for d in self.torneo._Torneo__disciplinas if d.obtenerNombre() == nombre_disciplina), None)

        if disciplina:
            print(disciplina)
        else:
            print("Disciplina no encontrada.")

    def mostrar_disciplinas_por_participante(self):
        nombre_participante = input("Ingrese el nombre del participante para ver disciplinas: ")
        participante = next((p for p in self.torneo._Torneo__participantes if p.obtenerNombre() == nombre_participante), None)

        if participante:
            disciplinas = participante.obtenerDisciplinas()
            if disciplinas:
                print(f"Disciplinas en las que participa {nombre_participante}:")
                for d in disciplinas:
                    print(d.obtenerNombre())
            else:
                print(f"{nombre_participante} no está inscrito en ninguna disciplina.")
        else:
            print("Participante no encontrado.")

    def ejecutar(self):
        self.crear_torneo()

        while True:
            print("\nOpciones:")
            print("1. Agregar disciplina")
            print("2. Agregar participante")
            print("3. Inscribir participante a disciplina")
            print("4. Ver participantes en una disciplina")
            print("5. Ver disciplinas de un participante")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_disciplina()
            elif opcion == '2':
                self.agregar_participante()
            elif opcion == '3':
                self.inscribir_participante()
            elif opcion == '4':
                self.mostrar_participantes_por_disciplina()
            elif opcion == '5':
                self.mostrar_disciplinas_por_participante()
            elif opcion == '6':
                break
            else:
                print("Opción inválida. Intente nuevamente.")

# main.py
if __name__ == "__main__":
    tester = Tester()
    tester.ejecutar()
