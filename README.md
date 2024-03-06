

<p align='center'>
<img src ="Diseño\HenryLogo.jpg">
<p>


<p align='center'>
<h2 style="text-align: center; border: none;">
 Proyecto integrador de Machine Learning y Endpoint en Fastapi
</h2>


 <h3 style="text-align: center; border: none;">
    Alumno: Hanson Veliendres Yataco >Data Sciencie>
</h3>




<h2 style="text-align: center; border: none;">
 <b>Análisis de Datasets Steam Australia </b>
</h2>


<p align='center'>
 <img src="Diseño/steam-logo-png-transparent.png" style="width: 30%;" alt="Steam Logo">
<p>


 <p style="text-align: left; border: none;">
<h3>
Steam pide que nos encarguemos de crear un sistema de recomendación de videojuegos para usuarios y se requieren funciones de filtrado(Endpoints), EDA, modelo de sentiment analysis NLP y modelo de ML para terminar con un MVP.<br>
Vamos a desarrollar este informe en los <b>4 pasos más importantes del desarrollo<b>
</h3>
</p>


 <h2 style="text-align: Left; border: none;">
    Como Primer Paso Limpiamos Extraemos y Transformamos la DATA.
</h2>
<h1>ETL y EDA</h1>
<p align='center'>
<img src ="Diseño\archivos.jpg">
<p>
<h3 style="text-align: left; border: none;">Se toman los 3 archivos JSON que nos fueron provistos, debido al tamaño y la complejidad de estos, lo siguiente fue convertirlos a archivos parquet, como se puede ver en el archivo <a href="https://github.com/hansonvel96/PI01_Steam_MLops/blob/master/Analisis/ETL.ipynb">ETL</a> que se encuentra en la carpeta <a href="https://github.com/hansonvel96/PI01_Steam_MLops/tree/master/Analisis">analisis</a>
<br>
</h3>
<p align='center'>
<img src ="Diseño\archivos2.jpg">
<p>

<h3>
Como se pudo ver en el ETL de ahi creamos 3 archivos parquet, luego estos los convertimos en un archivo llamado df_merge.parquet y developer.parquet estos los almacenamos en la carpeta <a href="https://github.com/hansonvel96/PI01_Steam_MLops/tree/master/Data">data</a>, que son consumidos por las funciones y por el modelo de entrenamiento como vamos a pasar a mostrar luego.
</h3>

<p style="text-align: left; border: none;">
<h3>Se hace un informe <a href="https://github.com/hansonvel96/PI01_Steam_MLops/blob/master/Analisis/EDA.ipynb">EDA</a>, que se encuentra en la carpeta ANALISIS , tomando cada uno de los datasets provistos y analizando las variables de cada uno de los Endpoints, estos son:</h3><br>
<h3>Developer:</h3> Nos muestra la cantidad de ítems y porcentaje de contenido Free por año según empresa desarrolladora.<br>
<h3>UserData:</h3> Observa el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br><br>
<h3>User For Genre:</h3> Observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de ítems que tiene el mismo. <br><br>
<h3>Best Developer Year:</h3> Muestra el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. <br><br>
<h3>Developer Reviews Analysis:</h3> Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave
y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados
con un análisis de sentimiento como valor positivo o negativo. <br><br>
<h3>Recomendación:</h3> Es el modelo de Machine Learning que observa el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de ítems que tiene el mismo.
<br><br>
<h3>Para lograr los Analisis de los dataset, tomamos las columnas pertinentes que sean necesarias para la creacion de funciones y las analizamos individualmente y a efectos de poder ejecutar los Endpoints Apis, se crean <a href="https://github.com/hansonvel96/PI01_Steam_MLops/blob/master/Functions.py">funciones</a> para poder consumir los dataset y obtener las respuestas esperadas segun lo propuesto.<br><br></h3>


 <h2 style="text-align: Left; border: none;">
    Como Segundo Paso
</h2>
<h1>Se Crea un entorno virtual en FastApi</h1>
<h4>La aplicación para el deploy elegida es FastApi, donde primero en un entorno virtual local, hacemos las comprobaciones de que las funciones ejecuten de manera local correctamente.</h4><br>
</p>
<p align='center'>
<a href="https://pi01-steam-mlops-31re.onrender.com/docs"><img alt="Fastapi" src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" style="display: inline-block; width: 200px;"></a>
</p>
<p align='center'>Click en la imagen para ir al deploy en Render</p>


<p align='center'>
<img src ="Diseño\fastapiendpoints.jpg" style="width: 60%;">
</p>


<p>
Para llegar a este resultado, en primer lugar creamos el entorno virtual en una carpeta separada del proyecto que se sube a Github, esto para, por error, no subir la carpeta ya que el espacio es limitado en el Push y puede fallar.<br>
Además cada vez que hacemos un deploy en render si falla, cancela el mismo, lo que consume mucho tiempo.
</p>
<p align='center'>
<img src ="Diseño\entorno.jpg" style="width: 30%;">
</p>
<p>
En este se cargan los archivos necesarios para correr la API, es una manera más ordenada de trabajar y optimizar recursos.
</p>
<p>
Se crea un archivo <a href="https://github.com/hansonvel96/PI01_Steam_MLops/blob/master/main.py">main.py</a> que es el que maneja el entorno de FastApi, este importa las funciones de <a href="https://github.com/hansonvel96/PI01_Steam_MLops/blob/master/Functions.py">Functions.py</a> donde en este archivo hacemos las consultas únicamente, dejando mas simple de leer el archivo.
</p>


<p align='center'>
<img src ="Diseño\enpoint.jpg" style="width: 60%;">
</p>


 <h2 style="text-align: Left; border: none;">
    A Continuación como Tercer Paso
</h2>
<p>
<h1>Creamos un Web Service en Render</h1>
</p>
<h4>La aplicación para el deploy en la nube elegida es Render, lugar donde se pueden hacer las consultas definitivas.</h4><br>
<h3>"Es Decir ya no localmente"</h3>
<p align='center'>
<a href="https://pi01-steam-mlops-31re.onrender.com"><img alt="Fastapi" src="https://intellyx.com/wp-content/uploads/2019/08/Render-cloud-intellyx-BC-logo.png" style="display: inline-block; width: 300px;"></a>
</p>
<p align='center'>Click en la imagen para ir al deploy en Render</p>
<p align='center'>
<img src ="Diseño\render.jpg" style="width: 60%;">
</p>
<h4>Se crea una página de inicio donde se puede ingresar a la API o a este repositorio</h4><br>
<p align='center'>
<img src ="Diseño\home.jpg" style="width: 60%;">
</p>
<h4>La metodología de uso es la misma que en el deploy local, dentro de cada endpoint hay instrucciones de como usar cada uno y una lista de sugerencias para probarlos.</h4><br>
<p align='center'>
<img src ="Diseño\consultas.jpg" style="width: 60%;">
</p>


 <h2 style="text-align: Left; border: none;">
    Cuarto Paso
</h2>
<p>
<h1>Creamos un video explicando el funcionamiento del deploy y el proyecto en sí</h1>
<p align='center'>
<a><img alt="Fastapi" src="https://logowik.com/content/uploads/images/google-drive-new9328.logowik.com.webp" style="display: inline-block; width: 300px;"></a>
</p>
<p align='center'>Click en la imagen para ir al drive del video</p>

 <h2 style="text-align: Left; border: none;">
    Aclaraciones
</h2>
<p>
<h1>Explicación GitHub</h1>
<p align='center'>
<img src ="Diseño\github.jpg" style="width: 60%;">
</p>
<p style="text-align: left; border: none;">
<h3>Como vemos la primer carpeta Analisis , contiene los informes <b>EDA<b> y <b>ETL<b> </h3>
<h3>La segunda carpeta Data, contiene los datasets necearios para el funcionamiento de la API</h3>
<h3>La tercer carpeta Diseño , contiene las imagenes usadas en este README</h3>

.gitignore es un archivo de uso interno de Git que nos permite usar archivos en nuestra computadora, pero, ser ignorados para subir al repositorio (git push), ya que lo que tenemos local funciona en sincronía con lo que se encuentra online<br><br>
Functions.py Es el archivo que contiene las funciones para las consultas, se mantiene en el main para que pueda operar de mejor manera la API.<br><br>
Readme.md Es el archivo que estamos observando en este momento, este tipo de archivo sirve para detallar, hacer explicaciones y presentaciones breves del repositorio. <br><br>
Main.py Es el archivo que hace que FastApi para pueda funcionar, donde colecciona las funciones y hace el deploy. <br><br>
Requirements.txt Carga las librerías de python y FastApi necesarias para poder correr el deploy en Render  .<br><br>

<h1>Datasets</h1>
<h3>
Como vemos dentro de la carpeta Data, los tres datasets que se usan para el funcionamiento de esta API son:
</h3>
<p align='center'>
<img src ="Diseño\dataset.jpg">
</p>
<h3>datos_entrenamiento.pkl:</h3> Dataset que contiene en formato comprimido los datos del modelo de entrenamiento para poder ser consumidos por el Endpoint de Recomendacion.<br>
<h3>developer.parquet:</h3> Dataset que se creo para el uso del Endpoint, Developer, por problemas a la hora de la lectura del dataset df_merge.<br>
<h3>df_merge.parquet:</h3> Dataset creado desde el merge de los 3 dataset individuales, es consumido por el resto de los Endpoints. <br>

