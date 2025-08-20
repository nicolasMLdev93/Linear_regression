from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd
from sklearn import linear_model

# Modelo de regresión lineal
reg = linear_model.LinearRegression()

# Archivo csv limpio
dataset = pd.read_csv('../data/clean_dataframe.csv')
X_test = dataset.iloc[:, 0:4]
Y_test = dataset.iloc[:, -1]

# Entrena el modelo
reg.fit(X_test, Y_test)

# Predicciones sobre los datos de test
Y_pred = reg.predict(X_test)

# Cálculo de métricas
# R² (coeficiente de determinación)
# Mide qué tan bien el modelo explica la variación de los datos reales.
# Valor entre 0 y 1, más cerca de 1 significa mejor ajuste.
r2 = r2_score(Y_test, Y_pred)

# MAE (Mean Absolute Error / Error Absoluto Medio)
# Es el promedio de la diferencia absoluta entre los valores reales y los predichos.
# Indica en promedio cuánto se equivoca el modelo en la unidad de la variable.
mae = mean_absolute_error(Y_test, Y_pred)

# MSE (Mean Squared Error / Error Cuadrático Medio)
# Es el promedio de las diferencias al cuadrado entre predicciones y valores reales.
# Penaliza más los errores grandes.
mse = mean_squared_error(Y_test, Y_pred)

# RMSE (Root Mean Squared Error / Raíz del Error Cuadrático Medio)
# Es la raíz cuadrada del MSE, para que esté en la misma unidad que la variable original.
rmse = np.sqrt(mse)

# Mostrar resultados
print("=== Resultados del modelo ===")
print("Predicciones:")
print(Y_pred)
print("\nValores reales:")
print(Y_test.values)

print("\n=== Coeficientes e Intercepto ===")
print(f"Coeficientes: {reg.coef_}")  # Coeficientes de cada variable independiente (b1,b2,b3,b4)
print(f"Intercepto: {reg.intercept_}")  # Intercepto (b0) de la regresión

print("\n=== Métricas ===")
print(f"R²: {r2:.4f}")
print(f"MAE: {mae:.4f}")
print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
