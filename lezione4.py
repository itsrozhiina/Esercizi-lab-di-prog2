import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def simula_lanci(N):
    lanci = np.random.randint(0,2,N)
    testa_perc=np.mean(lanci) *100
    return testa_perc

sample_sizes = np.linspace(10 , 20000 , 100 ,dtype=int)

frequenze =[]

for N in sample_sizes:
    freq = simula_lanci(N)
    frequenze.append(freq)


plt.figure(figsize=(10,5))
plt.plot(sample_sizes , frequenze , label ='percente di testa')
plt.axhline(y=50,color='red' , linestyle='--' , label ='probabilita teorica')
plt.xlabel('numero di lanci')
plt.ylabel('frequenza 5 di teste')
plt.title('legge di grandi numeri')
plt.legend()
plt.show()



#  Caricamento del dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#  1. Quante righe e colonne ha il dataset?
print("Numero di righe e colonne:", df.shape)

#  2. Controlla quanti valori mancanti ci sono per colonna
print("\nValori mancanti per colonna:")
print(df.isnull().sum())

#  3. Riempi i valori mancanti nella colonna ‘Embarked’ con il valore più frequente
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

#  4. Rimuovi le righe dove il valore di ‘Age’ è mancante
df = df.dropna(subset=['Age'])
#  5. Controlla se ci sono righe duplicate
duplicati = df.duplicated().sum()
print("\nRighe duplicate:", duplicati)

# (Se vuoi rimuoverle)
df = df.drop_duplicates()

#  6. Calcola l’età media dei passeggeri per ogni classe
eta_media_per_classe = df.groupby('Pclass')['Age'].mean()
print("\nEtà media per classe:")
print(eta_media_per_classe)

#  7. Visualizza la distribuzione dell’età per classe
plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title("Distribuzione dell’età per classe")
plt.xlabel("Classe")
plt.ylabel("Età")
plt.grid(True)
plt.show()

#  8. Visualizza la distribuzione dell’età per classe divisa per sesso
plt.figure(figsize=(8, 5))
sns.boxplot(x='Pclass', y='Age', hue='Sex', data=df)
plt.title("Distribuzione dell’età per classe e sesso")
plt.xlabel("Classe")
plt.ylabel("Età")
plt.grid(True)
plt.show()


# Caricamento del dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head())

# 1. Esplora la distribuzione delle specie (quanti campioni ci sono per specie)
print("\nDistribuzione delle specie:")
print(df['species'].value_counts())

#  2. Calcola la lunghezza e la larghezza media dei petali per specie
print("\nLunghezza e larghezza media dei petali per specie:")
print(df.groupby('species')[['petal_length', 'petal_width']].mean())

# 3. Visualizza le dimensioni dei petali per specie (scatterplot)
plt.figure(figsize=(8, 5))
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df)
plt.title("Scatterplot delle dimensioni dei petali per specie")
plt.grid(True)
plt.show()

#  4. Crea una nuova colonna per l’area del petalo (lunghezza × larghezza)
df['petal_area'] = df['petal_length'] * df['petal_width']
print("\nColonna 'petal_area' aggiunta:")
print(df[['petal_length', 'petal_width', 'petal_area']].head())

#  5. Grafico della distribuzione dell'area del petalo per specie (boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(x='species', y='petal_area', data=df)
plt.title("Distribuzione dell’area del petalo per specie (Boxplot)")
plt.grid(True)
plt.show()

