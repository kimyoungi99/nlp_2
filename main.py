from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional 
import kb
from graph import create_graph
from actor_name_dict import get_dict
from actor_name_dict import get_reversed
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

dict = get_dict()
reversed_dict = get_reversed()
g = create_graph()

@app.post("/find_kevin_bacon_number")
async def find_kevin_bacon_number(request: Request, actor_name: str = Form(...)):
    path = kb.find_kevin_bacon_number_with_movies(g, 96659, reversed_dict[actor_name], dict)
    return templates.TemplateResponse("index.html", {"request": request, "path": path})

@app.get("/actors")
async def get_actors():
    return {"actors": list(reversed_dict.keys())}