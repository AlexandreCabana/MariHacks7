from fastapi import FastAPI, Request, Form, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


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
    parser(equation)
    return RedirectResponse("http://127.0.0.1:8000", status_code=status.HTTP_303_SEE_OTHER)


def parser(equation: str):
    nb_terme = 1
    for i in range(len(equation)):
        if equation[i] == '+' or equation[i] == '-':
            nb_terme += 1
    print(nb_terme)
