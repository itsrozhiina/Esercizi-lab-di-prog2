import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Dati da distribuzione gamma
x = gamma.rvs(a=1, size=1000)

# Istogramma e pdf teorica
plt.hist(x, bins=30, density=True)
plt.plot(np.linspace(0, max(x), 100), gamma.pdf(np.linspace(0, max(x), 100), 1))
plt.title("PDF gamma")
plt.show()

# varianza
print("Varianza:", np.var(x))

# parametro stimato
param = gamma.fit(x)
print("Parametro stimato:", param[0])

# CDF
plt.plot(np.linspace(0, max(x), 100), gamma.cdf(np.linspace(0, max(x), 100), *param))
plt.title("CDF gamma")
plt.show()
mesi = np.arange(12)
maxT = np.array([17,19,21,28,33,38,37,37,31,23,19,18])
minT = np.array([-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58])

# punti
plt.plot(mesi, maxT, 'ro')
plt.plot(mesi, minT, 'bo')
plt.show()

# fit lineare
a1, b1 = np.polyfit(mesi, maxT, 1)
a2, b2 = np.polyfit(mesi, minT, 1)
y1 = a1 * mesi + b1
y2 = a2 * mesi + b2

# errore medio assoluto (MAE)
print("MAE max:", np.mean(abs(maxT - y1)))
print("MAE min:", np.mean(abs(minT - y2)))

# errore quadratico medio (RMSE)
print("RMSE max:", np.sqrt(np.mean((maxT - y1)**2)))
print("RMSE min:", np.sqrt(np.mean((minT - y2)**2)))

import pandas as pd
from scipy.optimize import curve_fit

# funzione da stimare
def retta(x, m, q):
    return m * x + q

# dati
df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw')
x = df["disp"].values
y = df["mpg"].values

# stima parametri
popt, _ = curve_fit(retta, x, y)
m, q = popt

# previsione
y_stim = retta(x, m, q)

# stampa
print("Coefficiente angolare:", m)
print("Intercetta:", q)

# grafico
plt.scatter(x, y, label = "Dati", alpha = 0.4)
plt.plot(x, y_stim, color = "red", label = "Retta stimata")
plt.legend()
plt.title("Regressione MPG ~ DISP")
plt.show()

# errori
mae = np.mean(np.abs(y - y_stim))
rmse = np.sqrt(np.mean((y - y_stim)**2))

print("MAE:", mae)
print("RMSE:", rmse)
