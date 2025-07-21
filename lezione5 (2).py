import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#4 rispondere alle domande

sales = pd.DataFrame(
    data={
        "employee": [
            "Katrina",
            "Guanyu",
            "Jan",
            "Roman",
            "Jacqueline",
            "Paola",
            "Esperanza",
            "Alaina",
            "Egweyn",
        ],
        "sales": [14, 17, 6, 12, 8, 3, 7, 15, 5],
        "year": [2018, 2019, 2020, 2018, 2020, 2019, 2019, 2020, 2020],
    }
)
#vendite maggiore di 10

vendite_mag10 = sales[sales['sales']>10]
print('venite>10')
print(vendite_mag10)

#vendite per 2018
vendite_2018 = sales[sales['year']==2018]
print('\nvendite per 2018')
print(vendite_2018)

#vendite magiore 10 per 2018
maggiore_13 =vendite_mag10[vendite_mag10['year'] ==2018]
print('\n vendite>13 e anno =2018')
print(maggiore_13)

#tutto trane i casi in cui le vendite sono maggiore di 13 e l'anno e 2018
nuovo_sales = sales[~((sales['year']== 2018) & (sales['sales'] >13))]
print('\ntutti tranne anno = 2018 e vendite >13')
print(nuovo_sales)
#i dati dove le vendite divise per 3 sono maggiori di 3
diviso_3 = sales[sales['sales'] /3 >3]
print('\nvendite/3 >3')
print(diviso_3)
#i dipendenti i cui nomi sono dopo la j
dopo_j = sales[sales['employee']>'J']
print('\n dipendenti con nomi dopo J')
print(dopo_j)

#5 analisi di un dataset di video giochi


import seaborn as sns

# Caricamento del dataset
url = 'https://zenodo.org/record/5898311/files/vgsales.csv'
df = pd.read_csv(url)
print(df.head())

#1.quanti videogiochi sono stati pubblicati

somma = len(df)
print('numero totale di videogiochi:')
print(df.shape[0])
print(somma)

#2.quali sono i generi piu popolari
genre_counts = df['Genre'].value_counts()

plt.figure(figsize = (10 , 6))
plt.bar(genre_counts.index , genre_counts.values)
plt.title('numero di giochi per genere')
plt.xlabel('genere')
plt.ylabel('numero di giochi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#3 rivoluzione del numero di giochi pubblicati nel tempo

year_counts = df['Year'].value_counts().sort_index()

plt.figure(figsize=(10 , 6))
plt.plot(year_counts , year_counts.values , marker='o')
plt.title('numero di giochi pubblicati nel tempo')
plt.xlabel('anno')
plt.ylabel('numero di giochi')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#4 riproduzione del plot 
sales_by_genere = df.groupby('Genre')[['NA_Sales' , 'EU_Sales' , 'JP_Sales' , 'Other_Sales']].sum()
sales_by_genere['Total']=sales_by_genere.sum(axis=1)
sales_by_genere = sales_by_genere.sort_values(by='Total' , ascending = False)

plt.figure(figsize=(12 , 8))
sales_by_genere.plot(kind='bar' , stacked = True , figsize=(12 , 8) , colormap='tab10')
plt.title('vendite per regione per genere')
plt.xlabel('genere')
plt.ylabel('milioni di unita')
plt.legend(title='regione')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()