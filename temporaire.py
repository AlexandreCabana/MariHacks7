# TODO: Ajouter la simplification en evaluant la somme/multiplication de termes dans simplifier_immediatement.

def simplifier(expression):

    firstEnter = True
    nouvelleExpression = expression
    while nouvelleExpression != expression or firstEnter:

        firstEnter = False
        expression = nouvelleExpression

        while nouvelleExpression != False:
            expression = nouvelleExpression
            nouvelleExpression = simplifier_immediatement(expression)

        nouvelleExpression = expression

        for terme in range(len(expression)):
            nouvelleExpression[terme] = simplifier(nouvelleExpression[terme])

    return nouvelleExpression
