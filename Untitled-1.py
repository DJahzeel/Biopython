
# EJERICIO 2 - GENERA LA CLASE GEN CON AL MENOS 3 ATRIBUTOS,3 METODOS CONTANDO EL CONSTRUCTOR)
from random import choice, seed
class Gen ():
    # Atrivutos
        Nombre = 0
        Estructura = 0
        Funcion = 0
        # constructor
        def __init__(self, nombre,estructura,funcion):
            self.Nombre = nombre
            self.Estructura = estructura
            self.Funcion = funcion
        # Metodos
        def Adaptacion(self):
            adaptaciones = ["Mutación", "Selección natural", "Deriva genética"]
            return choice(adaptaciones)

        def Regulacion(self):
            regulaciones = ["Regulación positiva", "Regulación negativa", "Feedback"]
            return choice(regulaciones)
        
    
# Instancia 
Gen1 = Gen("ADN", "ATCG","Transcripción")
Gen1.Adaptacion()
Gen1.Regulacion()

print("Nombre:", Gen1.Nombre)
print("Secuencia:", Gen1.Estructura)
print("Función:", Gen1.Funcion)
print("Adaptación:", Gen1.Adaptacion())
print("Regulación:", Gen1.Regulacion())





