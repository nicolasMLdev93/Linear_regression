from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

# Crear el modelo
reg = linear_model.LinearRegression()

# Cargar dataset
dataset = pd.read_csv('../data/clean_dataframe.csv') 
X = dataset.iloc[:,0:4]
Y = dataset.iloc[:,-1]

# Entrenar el modelo
reg.fit(X, Y)

# Predicciones
Y_pred = reg.predict(X)

plt.figure(figsize=(10,6))
plt.scatter(Y, Y_pred, color='tab:blue', edgecolor='k', alpha=0.7, label='Valores reales')
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', lw=2, label='Predicciones del modelo')

# Etiquetas
plt.title('Predicción de demanda de energía', fontsize=16, fontweight='bold')
plt.xlabel('Demanda Real (MW)')
plt.ylabel('Demanda Predicha (MW)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Guardar gráfico 
plt.savefig('real_vs_predicho.png', dpi=300, bbox_inches='tight')

# Mostrar gráfico
plt.show()
