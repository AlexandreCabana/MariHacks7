class Solver:
    def solve(self, expression):
        self.expression = expression
        self.degre = self.finddegre()
        if self.degre == 1:
            return self.solvedegreoneequation()
    def finddegre(self):
        return max([i.degre for i in self.expression])

    def solvedegreoneequation(self):
        return -self.expression[1].coefficient/self.expression[0].coefficient

