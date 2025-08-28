import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from classes.data_processor import Energy_demand  

# Archivo csv limpio
dataset = pd.read_csv('../data/clean_dataframe.csv') 

def get_variables(dataset):
    # Dividimos el dataset en columnas con variables independientes (x1,x2,x3 y x4) y variables dependientes (y)
    # Variables independientes:
    X = dataset.iloc[:,0:4]
    # Variable dependiente:
    Y = dataset.iloc[:,-1]
    return X,Y
X = get_variables(dataset)[0]
Y = get_variables(dataset)[1]


# Crear instancia de la clase:
energy_instance = Energy_demand()

# Entrena el modelo:
energy_instance.train_model(X, Y)

def load_features():  
    temp_feature = float(input("Ingrese la temperatura en grados C (°C): "))
    
    day_feature = int(input("Ingrese el día de la semana (0 - lunes, 1 - martes, etc.): "))
    while day_feature < 0 or day_feature > 6:
        day_feature = int(input("Día inválido. Ingrese un valor entre 0 y 6: "))
    
    hour_feature = int(input("Ingrese la hora (formato HH 0 - 23): "))
    while hour_feature < 0 or hour_feature > 23:
        hour_feature = int(input("Hora inválida. Ingrese un valor entre 0 y 23: "))
    
    hum_feature = float(input("Ingrese el porcentaje de humedad (ej: 45.5): "))
    
    return [temp_feature, day_feature, hour_feature, hum_feature]  

features = load_features()

# Predice los datos (creamos un dataframa con pandas donde c/u de las columnas coincida con
# las columas que se usaron para entrenar el modelo)
columns = ["Temperatura_C", "Dia_Semana", "Hora", "Humedad_%"]
input_df = pd.DataFrame([features], columns=columns) 
resultado = energy_instance.predict_data(input_df)[0]

print(f"La predicción de demanda es: {resultado:.2f} MW")