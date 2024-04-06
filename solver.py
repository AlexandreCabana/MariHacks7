from math import sqrt
from terme import Terme


class Solver:
    def solve(self, expression):
        self.expression = expression.exprs
        self.degre = self.finddegre()
        self.sortequationbydegre()
        if self.degre == 1:
            return self.solvedegreoneequation()
        elif self.degre == 2:
            return self.solveseconddegreequation()
    def finddegre(self):
        return max([i.degre for i in self.expression])

    def sortequationbydegre(self):
        expression = []
        for i in range(self.degre, -1, -1):
            found=False
            for j in self.expression:
                if j.degre == i:
                    expression.append(j)
                    found=True
            if not found:
                expression.append(Terme(0,self.expression[-1].inconnue, i))
        self.expression = expression

    def solvedegreoneequation(self):
        return -self.expression[1].coefficient/self.expression[0].coefficient
    def solveseconddegreequation(self):
        a = self.expression[0].coefficient
        b = self.expression[1].coefficient
        c = self.expression[2].coefficient
        print(self.expression)
        print(a, b, c)
        if ((b**2-4*a*c)<=0):
            return None
        return (-b+sqrt(b**2-4*a*c))/(2*a),(-b-sqrt(b**2-4*a*c))/(2*a)
