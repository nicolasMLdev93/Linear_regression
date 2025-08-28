from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# Clase de Demanda de energía con métodos:
class Energy_demand:
    def __init__(self):
        self.model = LinearRegression()
    def train_model(self,x_train,y_train):
        # Entrenamiento del modelo
        self.model.fit(x_train,y_train)
    def predict_data(self,x_pred):
        # Determinación de nuevo dato
        y_pred = self.model.predict(x_pred)
        return y_pred
    def get_metrics(self,x_test,y_test):
        y_pred = self.model.predict(x_test)
        # Cálculo de métricas
        # R² (coeficiente de determinación)
        # Mide qué tan bien el modelo explica la variación de los datos reales.
        # Valor entre 0 y 1, más cerca de 1 significa mejor ajuste.
        r2 = r2_score(y_test, y_pred)

        # MAE (Mean Absolute Error / Error Absoluto Medio)
        # Es el promedio de la diferencia absoluta entre los valores reales y los predichos.
        # Indica en promedio cuánto se equivoca el modelo en la unidad de la variable.
        mae = mean_absolute_error(y_test, y_pred)

        # MSE (Mean Squared Error / Error Cuadrático Medio)
        # Es el promedio de las diferencias al cuadrado entre predicciones y valores reales.
        # Penaliza más los errores grandes.
        mse = mean_squared_error(y_test, y_pred)

        # RMSE (Root Mean Squared Error / Raíz del Error Cuadrático Medio)
        # Es la raíz cuadrada del MSE, para que esté en la misma unidad que la variable original.
        rmse = np.sqrt(mse)
        return r2,mae,mse,rmse

