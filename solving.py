from terme import Terme
from operations import Somme, Mult, Div
from simplifier import simplifier

# Fonction qui enleve toutes les divisions.
def enlever_divisions(expr1, expr2):

    while True:

        expr1 = simplifier(expr1)
        expr2 = simplifier(expr2)

        if isinstance(expr1, Div):
            expr2 = Mult(expr2.exprs, expr1.exprs[terme].denom)
            expr1 = expr1.exprs[terme].num

        elif isinstance(expr2, Div):
            expr1 = Mult(expr1.exprs, expr2.exprs[terme].denom)
            expr2 = expr2.exprs[terme].num

        else:
            noDivs = True
            
            if not isinstance(expr1, Terme):
                for terme in range(len(expr1.exprs)):
                    if isinstance(expr1.exprs[terme], Div) and noDivs:

                        noDivs = False
                        
                        temp = expr1.exprs[:]
                        temp.pop(terme)

                        expr2 = Somme([expr2, Mult([Terme(-1, "x", 0), Somme(temp)])])
                        expr2 = Mult([expr2, expr1.exprs[terme].denom])
                        
                        expr1 = expr1.exprs[terme].num

            
            if not isinstance(expr2, Terme):
                for terme in range(len(expr2.exprs)):
                    if isinstance(expr2.exprs[terme], Div) and noDivs:

                        noDivs = False
                        
                        temp = expr2.exprs[:]
                        temp.pop(terme)

                        expr1 = Somme([expr1, Mult([Terme(-1, "x", 0), Somme(temp)])])
                        expr1 = Mult([expr1, expr2.exprs[terme].denom])
                        
                        expr2 = expr1.exprs[terme].num
            
            if noDivs:
                break

    return (expr1, expr2)



