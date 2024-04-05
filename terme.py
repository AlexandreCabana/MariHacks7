class Terme:
    def __init__(self, coefficient: int, inconnue:str, degree: int):
        self.coefficient = coefficient
        self.inconnue = inconnue
        self.degree = degree

    def __add__(self, other):
        if self.degree == other.degree and self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient + other.coefficient, inconnue=self.inconnue, degree=self.degree)
        return None

    def __sub__(self, other):
        if self.degree == other.degree and self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient - other.coefficient, inconnue=self.inconnue, degree=self.degree)
        return None

    def __mul__(self, other):
        if self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient * other.coefficient, inconnue=self.inconnue, degree=self.degree + other.degree)
        return None
    def __truediv__(self, other):
        if self.inconnue == other.inconnue:
            return Terme(coefficient=self.coefficient / other.coefficient, inconnue=self.inconnue, degree=self.degree-other.degree)
        return None

    def __repr__(self):
        return f'Coefficient: {self.coefficient}, inconnue: {self.inconnue}, degree: {self.degree}'

    def __eq__(self, other):
        return self.coefficient == other.coefficient and self.inconnue == other.inconnue and self.degree == other.degree and self.degree
