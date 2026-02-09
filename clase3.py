# actividad 1
# Definimos las clases de las fuentes primero
class MP3:
    def reproducir(self):
        return "Sonando MP3"

class CD:
    def reproducir(self):
        return "Sonando CD"

class Consola:
    def reproducir(self):
        return "Sonando Consola"

class Reproductor:
    def __init__(self):
        self.fuente_actual = MP3()
        
    def cambiar_fuente(self, nueva_fuente):
        self.fuente_actual = nueva_fuente
        
    def reproducir(self):
        print(self.fuente_actual.reproducir())

# esta parte es la que no se puede tocar
reproductor = Reproductor()  
reproductor.reproducir()  # Salida: "Sonando MP3"

reproductor.cambiar_fuente(CD())  
reproductor.reproducir()  # Salida: "Sonando CD"

reproductor.cambiar_fuente(Consola())  
reproductor.reproducir()  # Salida: "Sonando Consola"