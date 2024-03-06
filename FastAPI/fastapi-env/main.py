from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app2 = FastAPI()

class Libro (BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app2.get("/")
def index ():
    return {"Message: Hola, Phytoniano"}

@app2.get("/libros/{id}")
def mostrar_libro (id:int):
    return {"data": id}

@app2.post("/libros")
def insertar_libro (libro: Libro):
    return {"message": f"libro {libro.titulo}insertado"}