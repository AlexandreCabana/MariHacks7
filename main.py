from fastapi import FastAPI, Request, Form, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import string
from terme import Terme

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
    print(equation)
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
    print(inconnue)
    print(degree)
    print(coefficient)
    print(terme)
    print(nb_terme)
    Terme(int(degree), inconnue, int(coefficient))

def parservalex(equation: str):
    termelist=[]
    for stringterme in equation.split("+"):
        if "*" in stringterme:
            terme1 = findterme(stringterme.split("*")[0])
            terme2 = findterme(stringterme.split("*")[1])
            termelist.append(terme1*terme2)
        else:
            termelist.append(findterme(stringterme))
    print(termelist)

def findterme(stringterme):
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
