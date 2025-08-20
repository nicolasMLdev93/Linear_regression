import pandas as pd
from scipy import stats
import numpy as np

# Importación del archivo .csv para la posterior limpieza de datos con Pandas.
dataset = pd.read_csv('dataframe_demandas.csv')

def process_dataset(df):
    # A modo de unificación de criterios, todos los strings en c/u de las columnas de los features se convierten a minúscula
    df['Dia_Semana'] = df['Dia_Semana'].str.lower() 

    # Cada día de la semana de la columna Dia_Semana se convierte en un número entero a modo de luego scikit-learn pueda procesar los 
    # datos de forma correcta.
    day_index:dict[str, int] = {
        'lunes':0,
        'martes':1,
        'miércoles':2,
        'jueves':3,
        'viernes':4,
        'sábado':5,
        'domingo':6
    }

    df['Dia_Semana'] = df['Dia_Semana'].map(day_index)

    # Eliminamos datos redundantes y nulos que no aportan al procesamiento de los datos
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Convergencia de tipo de datos para cada feature
    df['Temperatura_C'] = df['Temperatura_C'].astype(float).round(2) # Temperatura en °C a número de coma flotante
    df['Humedad_%'] = df['Humedad_%'].astype(float).round(2) # Humedad en porcentaje a número de coma flotante
    df['Demanda_MW'] = df['Demanda_MW'].astype(float).round(2) # Demanda en Megavatios a número de coma flotante

    # Z-SCORE (Unidad tipificada) utiliza el valor del feature que corresponde a determinda fila, le resta la media (promedio de la muestra)
    #  y el resultado lo divide por la Desviación Estándar (nos dice cuanto se desvían los datos con respecto a su media); de esta forma
    # filtra los datos que son extremos y pueden así afectar a nuestro modelo.
    df = df[(np.abs(stats.zscore(df['Demanda_MW'])) < 3)] 
    # ~68% de los datos están a 1 desviación estándar de la media
    # ~95% de los datos están a 2 desviaciones estándar
    # ~99.7% de los datos están a 3 desviaciones estándar
    
    return df

dataset_clean = process_dataset(dataset)
dataset_clean.to_csv('clean_dataframe.csv',index=False, encoding='utf-8-sig')










