import pandas as pd
from classes.data_processor import Energy_demand

# Obtengo las columnass para obtener las métricas
dataset = pd.read_csv('../data/clean_dataframe.csv')
X_test = dataset.iloc[:, 0:4]
Y_test = dataset.iloc[:, -1]

# Creo una instancia de la clase:
energy_instance = Energy_demand()

# Entrenar modelo
energy_instance.train_model(X_test, Y_test)

# Métricas:
metrics = energy_instance.get_metrics(X_test,Y_test)

# Intercepto y coeficientes
intercept = energy_instance.get_intercept()
coef = energy_instance.get_coef()

# Mostrar resultados
print("=== Resultados del modelo ===")
print("Predicciones:")

print("\n=== Coeficientes e Intercepto ===")
print(f"Coeficientes: {coef}")  # Coeficientes de cada variable independiente (b1,b2,b3,b4)
print(f"Intercepto: {intercept}")  # Intercepto (b0) de la regresión

print("\n=== Métricas ===")
print(f"R²: {metrics[0]:.4f}")
print(f"MAE: {metrics[1]:.4f}")
print(f"MSE: {metrics[2]:.4f}")
print(f"RMSE: {metrics[3]:.4f}")
