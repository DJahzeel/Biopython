
from random import choice, seed

class Gen:
    """
    Clase que representa un gen con atributos básicos y métodos
    para simular su adaptación y regulación.

    Atributos
    ----------
    nombre : str
        Nombre del gen.
    estructura : str
        Secuencia que compone el gen.
    funcion : str
        Función biológica del gen.
    """

    def __init__(self, nombre, estructura, funcion):
        """
        Inicializa una instancia de la clase Gen.

        Parámetros
        ----------
        nombre : str
            Nombre del gen.
        estructura : str
            Secuencia que compone el gen (por ejemplo: 'ATCG').
        funcion : str
            Función biológica del gen (por ejemplo: 'Transcripción').
        """
        self.nombre = nombre
        self.estructura = estructura
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


# Instancia de la clase
gen1 = Gen("ADN", "ATCG", "Transcripción")

print("Nombre:", gen1.nombre)
print("Secuencia:", gen1.estructura)
print("Función:", gen1.funcion)
print("Adaptación:", gen1.adaptacion())
print("Regulación:", gen1.regulacion())






