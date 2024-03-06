
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
            <p>Haciendo click en la imagen debajo <br> <a href="https://pi01-steam-mlops-31re.onrender.com/docs"><img alt="LinkedIn" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" style="display: inline-block; width: 200px;"></a><br> Ingresa a la api</p>
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


def UserData(User_id):
    df_merged = pd.read_parquet('Data/df_merge.parquet')
    
    user_data = df_merged[df_merged['user_id'] == User_id]

    # Calcular la cantidad de dinero gastado por el usuario
    total_spent = (user_data['price']).sum()

    # Calcular el porcentaje de recomendación en base a reviews.recommend
    recommend_percentage = df_merged[df_merged['user_id'] == User_id]['recommend'].mean() * 100

    # Calcular la cantidad de items
    num_items = len(user_data)

    # Construir el Resultado en el Formato Especificado
    resultado = {
        "Usuario": User_id,
        "Dinero gastado": f"{total_spent:.2f} AUD",
        "porcentaje de recomendación": f"{recommend_percentage:.2f}%",
        "Cantidad de items": num_items
    }
    return resultado



def UserForGenre(genero):

    ufg = pd.read_parquet('Data/df_merge.parquet')
    genero = genero.lower()
    genero = genero.capitalize()
    ufg['release_date'] = pd.to_datetime(ufg['release_date'], errors='coerce')
    max_horas_ano = None
    max_horas = 0
    max_user = None  # Nuevo: mantener un registro del usuario con más horas jugadas
    horas_por_ano = {}
    
    for index, row in ufg.iterrows():
        if genero in row['genres']:
            # Obtener el año de la fecha de lanzamiento
            year = row['release_date'].year
            
            # Sumar las horas jugadas
            horas_jugadas = row['playtime_forever']
            
            if year not in horas_por_ano:
                horas_por_ano[year] = 0
                
            horas_por_ano[year] += horas_jugadas
            
            if horas_por_ano[year] > max_horas:
                max_horas = horas_por_ano[year]
                max_horas_ano = year
                max_user = row['user_id']  # Nuevo: actualizar el usuario con más horas jugadas
    
    res = {
        "Año con más horas": max_horas_ano,
        "Total de horas sumadas": max_horas,
        "Usuario con más horas jugadas para Género": max_user 
    }

def best_developer_year(anio):
    # Cargar el DataFrame desde el archivo parquet
    df_merged = pd.read_parquet('Data/df_merge.parquet')
    
    # Convertir 'item_id' a object en ambos DataFrames
    df_merged['Sentiment_analysis'] = df_merged['Sentiment_analysis'].astype('int')
    df_merged['item_id'] = df_merged['item_id'].astype('object')
    
    df_merged['recommend'] = df_merged['recommend'].astype(bool)
    
    # Filtrar por el año dado
    df_filtered = df_merged[df_merged['Años'] == anio]

    # Filtrar por reviews positivas y recomendadas
    df_filtered = df_filtered[(df_filtered['recommend'] == True) & (df_filtered['Sentiment_analysis'] == 2)]

    # Contar el número de juegos recomendados por cada desarrollador
    developer_counts = df_filtered.groupby('publisher')['item_id'].nunique()

    # Obtener el top 3 de desarrolladores
    top_developers = developer_counts.nlargest(3)

    # Construir el resultado en el formato especificado
    resultado = [{"Puesto {}".format(i+1): developer} for i, developer in enumerate(top_developers.index)]
    cadena_json = json.dumps(resultado, indent=2)
    return (cadena_json)

def developer_reviews_analysis(desarrollador):
    # Cargar los DataFrames
    
    df_merged = pd.read_parquet('Data/df_merge.parquet')
 
    
    # Convertir 'item_id' a object en ambos DataFrames
    df_merged['Sentiment_analysis'] = df_merged['Sentiment_analysis'].astype('int')
    df_merged['item_id'] = df_merged['item_id'].astype('object')
        
    # Filtrar por el desarrollador dado
    df_filtered = df_merged[df_merged['developer'] == desarrollador]

    # Contar la cantidad de registros con análisis de sentimiento positivo y negativo
    sentiment_counts = df_filtered['Sentiment_analysis'].value_counts()

    # Construir el resultado en el formato especificado
    
    resultado = {
                 "Desarrollador": desarrollador,
                 'Positive': sentiment_counts.get(2, 0),
                 "Neutral" :sentiment_counts.get(1, 0),
                 'Negative': sentiment_counts.get(0, 0) 
                 }  
    resultado_converted = {key: value.tolist() if isinstance(value, np.int64) else value for key, value in resultado.items()}
    return resultado_converted

