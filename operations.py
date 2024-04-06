# Definition des operations.

class Somme:
    def __init__(self, exprs):
        self.exprs = exprs

class Mult:
    def __init__(self, exprs):
        self.exprs = exprs

class Div:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

