# Definition des operations.

class Somme:
    def __init__(self, exprs):
        self.exprs = exprs
    def __repr__(self):
        return "Somme" + str(self.exprs)

class Mult:
    def __init__(self, exprs):
        self.exprs = exprs
    def __repr__(self):
        return "Mult" + str(self.exprs)

class Div:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    def __repr__(self):
        return "Div[" + str(self.num) + "]/[" + str(self.denom) + "]"

