class Terme:
    def __init__(self, coefficient: int, inconnue:str, degre: int):
        self.coefficient = coefficient
        self.inconnue = inconnue
        self.degre = degre

    def __add__(self, other):
        if self.degre == other.degre and self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient + other.coefficient, inconnue=self.inconnue, degre=self.degre)
        return None

    def __sub__(self, other):
        if self.degre == other.degre and self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient - other.coefficient, inconnue=self.inconnue, degre=self.degre)
        return None

    def __mul__(self, other):
        if self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient * other.coefficient, inconnue=self.inconnue, degre=self.degre + other.degre)
        return Terme(coefficient=self.coefficient * other.coefficient, inconnue=self.inconnue+other.inconnue, degre=self.degre+other.degre)
    def __truediv__(self, other):
        if self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient / other.coefficient, inconnue=self.inconnue, degre=self.degre - other.degre)
        return None

    def __repr__(self):
        return f'Coefficient: {self.coefficient}, inconnue: {self.inconnue}, degree: {self.degre}'

    def __eq__(self, other):
        return self.coefficient == other.coefficient and self.inconnue == other.inconnue and self.degre == other.degre
