
import pickle
import pandas as pd
import numpy as np
import gzip
import json


def presentacion():
    return '''
    <html>
        <head>
            <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">
            <title>PIML Hanson Veliendres</title>
            <style>
                body {
                    background-color:#000000 ;
                    font-family: "Nunito", sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #ffffff;
                    text-align: center;
                }
                p {
                    color: #ffffff;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
                
            </style>
        </head>
        <body>
            <p align='center'>
            <img src ="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png" style="display: inline-block;">
            <p>
            <h1>Deploy Render API de consultas de la plataforma de juegos Steam</h1>
            <p>API de Steam donde se pueden hacer diferentes consultas sobre Endpoints de la plataforma de videojuegos.</p>
            <br>
            <p>Haciendo click en la imagen debajo <br> <a href="XXXXX"><img alt="LinkedIn" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" style="display: inline-block; width: 200px;"></a><br> Ingresa a la api</p>
            <br>
            <p> El desarrollo de este proyecto esta en</p>
            <p><a href="https://github.com/hansonvel96/PI01_Steam_MLops/tree/master"><img alt="GitHub" src="https://static-00.iconduck.com/assets.00/github-icon-2048x1988-jzvzcf2t.png" style=" width: 120px"></a></p>
            <p align='center'>GitHub</p>
        </body>
    </html>
    '''

def Developer(desarrollador):
    df_games = pd.read_parquet('developer.parquet')
    # Filtra el dataframe por desarrollador de interés
    data_filtrada = df_games[df_games['publisher'] == desarrollador]
    # Calcula la cantidad de items por año
    cantidad_por_año = data_filtrada.groupby(data_filtrada['release_date'].dt.year)['item_id'].count()
    # Calcula la cantidad de elementos gratis por año
    cantidad_gratis_por_año = data_filtrada[data_filtrada['price'] == 0].groupby(data_filtrada['release_date'].dt.year)['item_id'].count()
    # Calcula el porcentaje de elementos gratis por año
    porcentaje_gratis_por_año = (cantidad_gratis_por_año.all() / cantidad_por_año * 100).fillna(0).astype(int)
    
    # Formatea los años en el resultado
    cantidad_por_año_formatted = {year: count for year, count in cantidad_por_año.items()}
    porcentaje_gratis_por_año_formatted = {year: f"{value}%" for year, value in porcentaje_gratis_por_año.items()}
    
    result_dict = {
        'Cantidad por año': f"{cantidad_por_año_formatted}",
        'Porcentaje gratis por año': f"{porcentaje_gratis_por_año_formatted}"
    }
    
    return result_dict