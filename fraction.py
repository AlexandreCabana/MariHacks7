from fractions import Fraction


class Fraction:
    def __init__(self, numerator: int, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if self.denominator == other.denominator and isinstance(other, Fraction):
            return Fraction(self.numerator + other.numerator, self.denominator)
        elif self.denominator != other.denominator and isinstance(other, Fraction):
            multiplier = Fraction.PPCM(self.denominator, other.denominator)
            self.desimplify(multiplier/self.denominator)
            other.desimplify(multiplier/other.denominator)
            return Fraction(self.numerator + other.numerator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator / other.numerator, self.denominator / other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator / other, self.denominator / other)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    def __repr__(self):
        return f'Numerator: {self.numerator}, Denominator: {self.denominator}'

    def simplify(self):
        ans = self / int(Fraction.PGCD(self.numerator, self.denominator))
        self.numerator = int(ans.numerator)
        self.denominator = int(ans.denominator)
        return self

    def desimplify(self, multiplier):
        self.numerator *= multiplier
        self.denominator *= multiplier
        return self

    @staticmethod
    def PGCD(a, b):
        if (b == 0):
            return a
        else:
            r = a % b
            return Fraction.PGCD(b, r)

    @staticmethod
    def PPCM(a, b):
        p = a * b
        while (a != b):
            if (a < b):
                b -= a
            else:
                a -= b
        return p / a
