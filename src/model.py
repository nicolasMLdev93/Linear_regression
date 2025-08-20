from sklearn import linear_model
import pandas as pd
reg = linear_model.LinearRegression()

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

# Modelo de entrenamiento de Regresión Lineal
def train_model_LR(X,Y,reg):
    reg.fit(X, Y) # reg.fit() entrena el modelo de Regresión Lineal Múltiple con los valores que se le pasan por parámetros
    return reg
model_result = train_model_LR(X,Y,reg)

