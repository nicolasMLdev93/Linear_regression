📈 Predicción de Demanda de Energía con Regresión Lineal Múltiple

🤖 Sobre el proyecto:

Este proyecto utiliza Regresión Lineal Múltiple para predecir la demanda de energía (Demanda_MW, en megavatios) en función de variables como temperatura, día de la semana, hora y humedad.
El flujo del proyecto incluye la limpieza y procesamiento de datos, el entrenamiento del modelo, la predicción de demanda y el reporte de métricas de desempeño.
Este modelo permite a las compañías eléctricas planificar la generación de energía, optimizar recursos y reducir riesgos de cortes de suministro, ya que proporciona estimaciones precisas de la demanda según condiciones climáticas y temporales. Además, facilita la toma de decisiones estratégicas sobre la operación de plantas, mantenimiento y gestión de costos.

Para el desarrollo de este proyecto de Regresión Lineal, profundicé mis conocimientos en Álgebra Lineal apoyándome en libros como "Álgebra Lineal y sus Aplicaciones" de David C. Lay y "Matemáticas para Machine Learning" de Marc Deisenroth, con el objetivo de reforzar los conceptos fundamentales detrás del modelo.


📂 Estructura del proyecto:

venv/

classes/
    __init_.py
    data_processor.py

data/
    dataframe.csv
    clean_dataframe.csv
    dataframe_demandas.csv
    processed.py
    
models/
    metrics.py
    
reports/
    graphics.py
    
src/
    pycache/
    __init_.py
    evaluate.py
    model.py
    
readme.md

requirements.txt

⚡ Instalación y ejecución:

1- Clonación del repositorio en Github: 
 git clone https://github.com/nicolasMLdev93/Linear_regression_Python.git 

2- Creación de entorno virtual =>  python -m venv .venv

3- Activación del entorno virtual => .venv\Scripts\activate 

4- Instlación de dependencias => pip install -r requirements.txt 

5- Ejecutar scripts => python src/model.py

6- Predicción de resultados => python src/evaluate.py

📊 Informes y gráficos:

La carpeta reports/ contiene todo lo relacionado con informes y visualizaciones.

Al ejecutar el archivo graphics.py dentro de reports/, se generan y muestran los gráficos del modelo, como la relación entre variables y la predicción de demanda. También se genera una imágen del gráfico y se guarda en la misma carpeta.

🧑 Mi perfil:

https://www.linkedin.com/in/nicol%C3%A1s-bauz%C3%A1-48a8a0244/ 👈 – Sígueme para ver mis proyectos de desarrollo y ML. 🚀



