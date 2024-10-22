from prestamo import Prestamo
from socio import Socio
from libro import Libro
from datetime import date as Fecha
 

class Tester:
    
    def probarLibro(self):
        try:
            libro = Libro(nombre="Cien Años de Soledad", autor="Gabriel García Márquez", 
                          editorial="Sudamericana", categoria="A")
            print(f"Libro creado correctamente: {libro}")
            
        except:
            print(f"Error esperado al crear libro con categoría inválida:")
            
            
            
            
    def probarSocio(self):
        try:
            socio = Socio(nombre="Santiago Pérez", fechaNacimiento=Fecha(2000, 6, 15))
            print(f"Socio creado correctamente: {socio}")

            print(f"¿Está habilitado el socio? {socio.estaHabilitado()}")

            socio.establecerFechaPenalizacion(Fecha(2024, 10, 1))
            print(f"Fecha de penalización establecida: {socio.obtenerFechaPenalizacion()}")
            print(f"¿Está habilitado el socio? {socio.estaHabilitado()}")

        except:
            print(f"Error inesperado al probar Socio:")




    def probarPrestamo(self):
        try:

            libro = Libro(nombre="El Quijote", autor="Miguel de Cervantes", 
                          editorial="Francisco de Robles", categoria="B")
            
            socio = Socio(nombre="Ana Gómez", fechaNacimiento=Fecha(1998, 3, 22))

            prestamo = Prestamo(libro=libro, fechaPrestamo=Fecha.today(), cantDias=15, socio=socio)
            prestamo.establecerFechaDevolucion()
            print(f"Préstamo creado correctamente: {prestamo}")
            print(f"Fecha de devolución esperada: {prestamo.obtenerFechaDevolucion()}")

            print(f"¿Está atrasado el préstamo? {prestamo.estaAtrasado()}")

            print(f"Fecha de penalización (si aplica): {prestamo.penalizacion()}")

        except :
            print(f"Error inesperado al probar Préstamo")

if __name__ == "__main__":
    Tester.main()
    