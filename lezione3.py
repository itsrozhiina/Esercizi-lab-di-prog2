import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv")
#visualizzo i primi 10 paesi ordinati
top10_alcol =df.sort_values(by = 'total_litres_of_pure_alcohol' , ascending = False).head(10)
print(top10_alcol[['country' , 'total_litres_of_pure_alcohol']])

media_birra = df['beer_servings'].mean()
print(f"la media di birra: {media_birra:.2f}")

media_vino = df['wine_servings'].mean()
print(f'la media di vino : {media_vino:.2f}')

media_distillati =df['spirit_servings'].mean()
print(f'la media di spirits:{media_distillati:.2f}')

df['alcohol_index'] = (df['wine_servings']+df['beer_servings']+df['spirit_servings'])/3
print(df[['country','alcohol_index']])

max_alcol = df.loc[df['alcohol_index'].idxmax()]
print('paese con massimo alcol:' , max_alcol['country'])

birra_oltre100=df[df['beer_servings']>100]
print(birra_oltre100[['country' , 'beer_servings']])

# il grafico per 10 con consumo alcolo piu alto 

plt.figure(figsize=(10,5))
plt.bar(top10_alcol['country'] , top10_alcol['total_litres_of_pure_alcohol'] )
plt.title('i paesi con alto consumo')
plt.xlabel('paese')
plt.ylabel('litri di alcol puro')
plt.xticks(rotation = 45)
plt.show()

df_sorted = df.sort_values(by='wine_servings')
plt.figure(figsize=(10 , 5))
plt.plot(df_sorted['country'] , df['beer_servings'] , marker ='o')
plt.title('consumo di birra')
plt.xlabel('paesi')
plt.ylabel('consumo di birra')
plt.show()