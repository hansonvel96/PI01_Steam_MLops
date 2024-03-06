##Importamos
from Functions import presentacion
from fastapi import FastAPI
import Functions as Functions
from Functions import *
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
import numpy as np
import gzip
import json

#http://127.0.0.1:8000
#https://fastapi-app-vf4c.onrender.com

app = FastAPI()

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=[">Home<"])
def home():
    return presentacion()

@app.get(path='/developer',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br>
                4. Sugerencia de usuarios: Valve, Ubisoft, Capcom, Epic Games, Rockstar Games, Sega.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["<Consultas Developer>"])

def Developer(Desarrollador):
    resultadodeveloper = Functions.Developer(Desarrollador)
    return resultadodeveloper
developer = Developer('Valve')
print(developer)



@app.get(path = '/userdata',
          description=""" 
    <html>
        <body>
            <h1>INSTRUCCIONES</h1>
            <h3>
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. Observe el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.<br>
                4. Sugerencia de usuarios: BrainsAccount, 76561197970982479, UTNerd24, AVATAR715, tarjla.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["<Consultas de UserData>"])
def UserData(User_id):
    resultado = Functions.UserData(User_id)
    return resultado
User_id = UserData('BrainsAccount')

@app.get(path='/UserForGenre',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. El usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br>
                4. Sugerencia de usuarios: Action, Strategy, Simulation, Racing.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["<Consultas User For Genre>"])
def UserForGenre(Genero_Especificado):
    resultadoReview = Functions.UserForGenre(Genero_Especificado)
    return resultadoReview
ufg = UserForGenre('Strategy')


@app.get(path='/best_developer_year',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado<br>
                4. Ingrese un año para obtener el resultado.<br>
                5. Para cambiar de Año, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["<Consultas Best Developer Year>"])
def best_developer_year(Año):
    resultadoReview = Functions.best_developer_year(Año)
    return resultadoReview

años = best_developer_year(2005)
print(años)

@app.get(path='/developer_reviews_analysis',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: ffff00;">INSTRUCCIONES</h1>
            <h3 style="color: ffff00; font-family: 'Trebuchet MS';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave<br>
                   y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados<br> 
                   con un análisis de sentimiento como valor positivo o negativo.<br>
                4. Sugerencia de usuarios: Epic Games, Rockstar Games, Valve.<br>
                5. Para cambiar de Desarollador , copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["<Consultas Developer Reviews Analysis>"])

def developer_reviews_analysis(Desarrolladora):
    resultadoReview = Functions.developer_reviews_analysis(Desarrolladora)
    return resultadoReview
dra = developer_reviews_analysis('Valve')