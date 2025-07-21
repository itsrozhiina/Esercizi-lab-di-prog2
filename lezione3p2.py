import pandas as pd
from datasets import load_dataset
import numpy as np
import matplotlib.pyplot as plt

dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

df = df.dropna(subset = ['salary_year_avg'])
print(df.columns)

paese_group = df.groupby('job_country')

stipendio_medio = paese_group['salary_year_avg'].mean()

job_count = paese_group.size()

stipendio_min = paese_group['salary_year_avg'].min()

stipendio_max = paese_group['salary_year_avg'].max()

riassunto=pd.DataFrame({
    'stipendio medio' :stipendio_medio,
    'job count' : job_count,
    'stipendio minimo' : stipendio_min,
    'stipendio massimo' : stipendio_max

}) .sort_values(stipendio_medio, ascending = False)

print('analisi per paesi: ')
print(riassunto)

stipendi_per_ruolo = df.groupby('job_title_short')['salary_year_avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
stipendi_per_ruolo.plot(kind='barh', color='skyblue')
plt.xlabel('Stipendio medio annuale (€)')
plt.ylabel('Titolo di lavoro')
plt.title('Stipendio medio per ruolo (ordinato)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

