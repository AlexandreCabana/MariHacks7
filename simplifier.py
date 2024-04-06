from terme import Terme
from operations import Somme, Mult, Div

# Definition de la fonction de une etape de simplification. Retourne l'expression simplifiee d'une etape s'il y a une simplification a faire, retourne False sinon.
def simplifier_immediatement(expression_input):

    if isinstance(expression_input, Somme):

        # Copier expression_input. (On n'est jamais trop sur!)
        expression = Somme(expression_input.exprs[:])

        # Utiliser la regle d'associativite.
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Somme):
                
                liste = expression.exprs[terme].exprs[:]
                expression.exprs.pop(terme)
                expression.exprs += liste

                # On a fait une etape, on termine.
                return expression

        # Evaluer des valeurs si possible, en premier en notant tous les termes, en deuxieme en essayant d'additionner les termes.
        aRajouter = []
        termes = []
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Terme):
                termes.append(terme)

        termesBackup = termes[:]

        while len(termes) > 1:
            
            termesAdditionnes = []
            somme = Terme(0, "x", 0)
            for terme in range(len(termes)):
                
                nouvelleSomme = somme + expression.exprs[termes[terme]]
                if nouvelleSomme:
                    somme = nouvelleSomme
                    termesAdditionnes.append(terme)

            for terme in termesAdditionnes[::-1]:
                termes.pop(terme)

            aRajouter.append(somme)

        if len(aRajouter) < len(termesBackup):

            if termes:
                aRajouter.append(expression.exprs[termes[0]])

            for terme in termesBackup[::-1]:
                expression.exprs.pop(terme)

            for terme in aRajouter:
                expression.exprs.append(terme)

            # On a fait une etape, on retourne.
            return expression


    if isinstance(expression_input, Mult):

        # Copier expression_input. (On n'est jamais trop sur!)
        expression = Mult(expression_input.exprs[:])

        # Utiliser la regle d'associativite.
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Mult):
                
                liste = expression.exprs[terme].exprs[:]
                expression.exprs.pop(terme)
                expression.exprs += liste
                
                # On a fait une etape, on termine.
                return expression

        # Evaluer des valeurs si possible, en premier en notant tous les termes, en deuxieme en essayant de multiplier les termes.
        termes = []
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Terme):
                termes.append(terme)

        if len(termes) > 1:
            resultat = Terme(1, "x", 0)
            for terme in termes:
                resultat *= expression.exprs[terme]

            for terme in termes[::-1]:
                expression.exprs.pop(terme)

            expression.exprs.append(resultat)

            # On a fait une etape, on termine.
            return expression

            
        # Sinon, utiliser la distributivite.
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Somme):
                
                listeSansTerme = expression.exprs[:]
                listeSansTerme.pop(terme)

                nouvelleListe = []
                for x in expression.exprs[terme].exprs:
                    nouvelleListe.append(Mult([x] + listeSansTerme))

                # Ne pas oublier de redefinir le type de expression a Somme!
                expression = Somme(nouvelleListe)

                # On a fait une etape, on termine.
                return expression
        
        # Sinon, entrer dans une divisions.
        for terme in range(len(expression.exprs)):
            if isinstance(expression.exprs[terme], Div):

                listeSansTerme = expression.exprs[:]
                listeSansTerme.pop(terme)

                numerateur = expression.exprs[terme].num
                denominateur = expression.exprs[terme].denom

                expression = Div(Mult(listeSansTerme + [numerateur]), denominateur)

                # On a fait une etape, on termine.
                return expression

    # Vu que rien n'a ete fait, on retourne False.
    return False

# Definition de la fonction de simplification. Se contente de simplifier l'expression, et de la retourner, voila tout.
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
