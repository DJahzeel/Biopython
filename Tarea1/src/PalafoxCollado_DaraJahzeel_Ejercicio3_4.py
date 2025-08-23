
from random import choice, seed

class Gen:
    """
    Clase que representa un gen con sus atributos y métodos.
    Atributos
    ----------
    nombre : str
        Nombre del gen.
    estructura : str
        Secuencia que compone el gen.
    funcion : str
        Función biológica del gen.
    """
    def __init__(self, nombre, secuencia, funcion):
        self.nombre = nombre
        self.secuencia = secuencia
        self.funcion = funcion

    def adaptacion(self):
        """
        Devuelve una adaptación aleatoria del gen.

        Returns
        -------
        str
            Una de las siguientes adaptaciones:
            "Mutación", "Selección natural" o "Deriva genética".
        """
        adaptaciones = ["Mutación", "Selección natural", "Deriva genética"]
        return choice(adaptaciones)

    def regulacion(self):
        """
        Devuelve un tipo de regulación aleatoria del gen.

        Returns
        -------
        str
            Una de las siguientes regulaciones:
            "Regulación positiva", "Regulación negativa" o "Feedback".
        """
        regulaciones = ["Regulación positiva", "Regulación negativa", "Feedback"]
        return choice(regulaciones)

class tRNA(Gen):
    "clase que representa un ARN de transferencia (tRNA) que hereda de la clase Gen con un atributo adicional y un método"
    def __init__(self, nombre, secuencia, funcion, anticodon):
        Gen.__init__(self, nombre, secuencia, funcion)
        self.anticodon = anticodon

    def longitud(self):
        return len(self.secuencia)


class RNANoCodificante(Gen):
    "clase que representa un ARN no codificante que hereda de la clase Gen con un atributo adicional = tipo"
    def __init__(self, nombre, secuencia, funcion, tipo):
        Gen.__init__(self, nombre, secuencia, funcion)
        self.tipo = tipo

class Proteina(tRNA):
    "clase que representa una proteína que hereda de la clase tRNA con un atributo adicional = aminoacidos y un método"
    def __init__(self, nombre, secuencia, funcion, anticodon, aminoacidos):
        super().__init__(nombre, secuencia, funcion, anticodon)
        self.aminoacidos = aminoacidos

    def longitud(self):
        "regresa numero de nucleotidos y aminoacidos"
        num_nucleotidos = len(self.secuencia)
        num_aminoacidos = len(self.aminoacidos.split('-'))
        return num_nucleotidos, num_aminoacidos

# Instancia de la clase
gen1 = Gen("ADN", "ATCG", "Transcripción")

print("GEN:", gen1.nombre,gen1.secuencia,gen1.funcion)
print("Adaptación:", gen1.adaptacion())
print("Regulación:", gen1.regulacion())

trna1 = tRNA("tRNA", "AUGC", "Traducción", "UAC")
print("\ntRNA:", trna1.nombre, trna1.secuencia, trna1.funcion, trna1.anticodon)
print("longitud:", trna1.longitud())

rna1 = RNANoCodificante("miRNA", "AUGCUA", "Regulación génica", "microRNA")
print("\nRNA No Codificante:", rna1.nombre, rna1.secuencia, rna1.funcion, rna1.tipo)

Proteina1 = Proteina("Hemoglobina", "AUGCUAGCUA", "Transporte de oxígeno", "UAC", "GLY-ALA-SER")
print("\nProteina:", Proteina1.nombre, Proteina1.secuencia, Proteina1.funcion, Proteina1.anticodon, Proteina1.aminoacidos)
print("longitud (nucleotidos, aminoacidos):", Proteina1.longitud())



