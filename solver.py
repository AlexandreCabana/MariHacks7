from math import sqrt


class Solver:
    def solve(self, expression):
        self.expression = expression.exprs
        self.degre = self.finddegre()
        self.sortequationbydegre()
        if self.degre == 1:
            return self.solvedegreoneequation()
        elif self.degre == 2:
            return self.solvedegreoneequation()
    def finddegre(self):
        return max([i.degre for i in self.expression])

    def sortequationbydegre(self):
        expression = []
        for i in range(self.degre, -1, -1):
            for j in self.expression:
                if j.degre == i:
                    expression.append(j)
        self.expression = expression

    def solvedegreoneequation(self):
        return -self.expression[1].coefficient/self.expression[0].coefficient
    def solveseconddegreequation(self):
        a = self.expression[0].coefficient
        b = self.expression[1].coefficient
        c = self.expression[2].coefficient
        return ((b+sqrt((b**2-4*a*c)))/(2*a),(b-sqrt((b**2-4*a*c)))/(2*a))

