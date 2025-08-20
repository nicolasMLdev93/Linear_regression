from sklearn import linear_model
import pandas as pd
from model import model_result

features:list = []

def load_features(f):  
    temp_feature = float(input("Ingrese la temperatura en grados C (°C): "))
    day_feature = int(input("Ingrese el día de la semana (0 - lunes, 1 - martes, etc.): "))
    hour_feature = int(input("Ingrese la hora (formato HH 0 - 23): "))
    hum_feature = float(input("Ingrese el porcentaje de humedad (ej: 45.5): "))
    
    f[:] = [temp_feature, day_feature, hour_feature, hum_feature]  

load_features(features)

def evaluate_model(model, f):
    columns = ["Temperatura_C", "Dia_Semana", "Hora", "Humedad_%"]
    input_df = pd.DataFrame([f], columns=columns)
    prediction = model.predict(input_df)
    return prediction[0]

resultado = evaluate_model(model_result, features)
print(f"La predicción de demanda es: {resultado:.2f} MW")
