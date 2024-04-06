from fastapi import FastAPI, Request, Form, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import string
from terme import Terme
from operations import Somme, Div, Mult
from simplifier import simplifier

alphabets = list(string.ascii_letters)

templates = Jinja2Templates(directory="html")
app = FastAPI()

app.mount("/css", StaticFiles(directory="css"), name="css")
#app.mount("/Image", StaticFiles(directory="Image"), name="Image")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def solve_equation(request: Request, equation: str = Form(...)) -> RedirectResponse:
    parservalex(equation)
    return RedirectResponse("http://127.0.0.1:8000", status_code=status.HTTP_303_SEE_OTHER)


def parser(equation: str):
    #equation_parser = [Terme(3,"x",1)]
    terme = ""
    equation = list(equation)

    #trouver le nombre de Terme
    for i in range(len(equation)):
        if equation[i] == '+' or equation[i] == '-':
            nb_terme += 1
    terme = equation[0:equation.index('+')]
    inconnue = ''
    degree = 1
    for i in range(len(terme)):
        for j in range(len(alphabets)):
            if terme[i] == alphabets[j]:
                inconnue = terme[i]
        if terme[i] == '^':
            degree = "".join(terme[terme.index('{')+1 : terme.index('}')])

    if inconnue == '':
        degree = 0
    coefficient = "".join(terme[0:terme.index(inconnue)])
    Terme(int(degree), inconnue, int(coefficient))

def parservalex(equation: str):
    equalite = equation.split("=")
    termelist=[]
    equation = regler_les_moin(equalite[0])
    for stringterme in equation.split("+"):
        if "*" in stringterme:
            terme1 = findterme(stringterme.split("*")[0])
            terme2 = findterme(stringterme.split("*")[1])
            termelist.append(Mult[terme1,terme2])
        else:
            termelist.append(findterme(stringterme))
    termelist2=[]
    equalite = regler_les_moin(equalite[1])
    for stringterm2 in equalite.split("+"):
        if "*" in stringterme:
            terme1 = findterme(stringterm2.split("*")[0])
            terme1.coefficient = -terme1.coefficient
            terme2 = findterme(stringterm2.split("*")[1])
            terme2.coefficient = -terme2.coefficient
            termelist2.append(Mult[terme1,terme2])
        else:
            a = findterme(stringterm2)
            a.coefficient = -a.coefficient
            termelist.append(a)
    print(simplifier(Somme(termelist)))

def findterme(stringterme:str):
        inconnue= None
        degre = None
        for letter in alphabets:
            if letter in stringterme:
                inconnue = letter
        if '^' in stringterme:
            degre = "".join(stringterme[stringterme.index('{')+1 : stringterme.index('}')])
        if inconnue is None and degre is None:
            return Terme(int(stringterme),"",0)
        elif degre is None:
            return Terme(int(stringterme[0:stringterme.index(inconnue)]),inconnue,1)
        else:
            return Terme(int(stringterme[0:stringterme.index(inconnue)]),inconnue,degre)

def regler_les_moin(equation:str)->str:
        ofsset = 0
        equation = list(equation)
        ans = equation.copy()
        for index, value in enumerate(equation):
            if value == "-":
                ans.insert(index + ofsset, "+")
                ofsset += 1

        equation = "".join(ans)
        return equation
