"""
FUNCIONES CREADAS PARA EL PROYECTO FINAL INDIVIDUAL 1 DE DATA SCIENCE DE SOY HENRY
                            - STEAM GAMES - 

FUNCIONES PARA ALIMENTAR LA API
"""

from fastapi import FastAPI
import Functions
from Functions import *
from fastapi.responses import HTMLResponse

#http://127.0.0.1:8000
#https://fastapi-app-vf4c.onrender.com

app = FastAPI()

@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Home"])
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
         tags=["Consultas Developer"])

def Developer(Desarrollador):
    resultadodeveloper = Functions.Developer(Desarrollador)
    return resultadodeveloper
developer = Developer('Valve')
print(developer)