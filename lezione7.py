import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Caricamento dati
df = pd.read_csv("data.csv")

# Colonna numerica per i mesi
df["mese_numerico"] = np.arange(len(df))

# Variabili
x = df[["mese_numerico"]]
y = df["passengers"]

# Regressione polinomiale (grado 3 per esempio)
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

modello = LinearRegression()
modello.fit(x_poly, y)

# Predizione
y_pred = modello.predict(x_poly)

# RMSE
rmse = np.sqrt(mean_squared_error(y, y_pred))
print("RMSE:", rmse)

# Grafico semplice con matplotlib
plt.plot(df["mese_numerico"], y, label="reali")
plt.plot(df["mese_numerico"], y_pred, label="stimati")
plt.legend()
plt.title("Passeggeri nel tempo")
plt.xlabel("Mese numerico")
plt.ylabel("Passeggeri")
plt.show()
