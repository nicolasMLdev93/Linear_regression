import pandas as pd

# Objeto para crear el DataFrame
data = {
    "Temperatura_C": [
        24.5, 21.3, 25.2, 29.6, 20.8, 22.1, 23.5, 19.7, 18.9, 26.3,
        27.5, 22.8, 24.0, 21.5, 28.2, 23.1, 25.7, 20.4, 19.9, 26.8,
        22.5, 24.7, 27.1, 23.9, 21.8, 28.5, 26.0, 25.4, 20.2, 29.0,
        23.3, 24.9, 27.8, 22.0, 21.2, 26.5, 25.9, 23.6, 20.7, 28.8,
        22.4, 24.1, 27.3, 21.7, 23.8, 26.9, 25.5, 22.6, 28.0, 24.3
    ],
    "Dia_Semana": [
        "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Lunes", "Martes", "Miércoles",
        "Jueves", "Viernes", "Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado",
        "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Lunes", "Martes",
        "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
        "Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo", "Lunes"
    ],
    "Hora": [
        8, 6, 12, 20, 17, 14, 10, 22, 9, 16,
        7, 15, 11, 19, 13, 21, 18, 5, 23, 12,
        8, 16, 14, 10, 9, 18, 20, 13, 6, 22,
        7, 15, 11, 17, 12, 19, 21, 14, 8, 20,
        9, 16, 13, 10, 18, 12, 15, 11, 22, 17
    ],
    "Humedad_%": [
        47, 61, 76, 78, 40, 55, 60, 65, 50, 70,
        45, 58, 63, 72, 49, 66, 59, 52, 68, 71,
        60, 57, 62, 64, 53, 69, 73, 61, 54, 67,
        56, 59, 65, 48, 51, 70, 74, 62, 55, 68,
        60, 63, 67, 50, 58, 71, 69, 54, 72, 61
    ],
    "Demanda_MW": [
        84.3, 93.8, 87.8, 127.7, 128.4, 90.5, 110.2, 99.3, 85.0, 120.1,
        88.4, 102.5, 95.6, 119.3, 107.2, 111.5, 98.6, 89.7, 116.0, 123.4,
        101.2, 94.8, 108.6, 97.5, 92.1, 121.0, 115.3, 109.4, 87.9, 125.6,
        103.5, 99.2, 117.8, 95.4, 90.7, 122.3, 118.5, 106.2, 88.9, 124.0,
        97.8, 100.5, 113.6, 91.7, 105.4, 119.9, 110.8, 96.3, 126.2, 102.7
    ]
}      

dataframe = pd.DataFrame(data)

# Dataframe guardado en un archivo CSV
dataframe.to_csv("dataframe_demandas.csv", index=False, encoding='utf-8-sig')
