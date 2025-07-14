
# ===============================
# Lezione 2 - Programmazione
# Autrice: Rozhina
# ===============================

import numpy as np
import random

# === 1. Indicizzazione booleana ===

# 1. Vettore con numeri primi tra 0 e 20
primi = np.array([2, 3, 5, 7, 11, 13, 17, 19])

# 2. Seleziona numeri maggiori di 10
maggiori_10 = primi[primi > 10]

# 3. Seleziona numeri primi pari
primi_pari = primi[primi % 2 == 0]

# === 2. Operazioni su array 2D ===

a = np.arange(1, 21).reshape(5, 4)
b = a[[1, 3], :]  # 2a e 4a riga
c = a[2, :]       # solo la 3a riga
divisione = a / c

# === 3. Seleziona valore vicino a 0.5 ===

arr = np.random.rand(10, 3)
vicini_05 = arr[np.arange(10), np.abs(arr - 0.5).argmin(axis=1)]

# === 4. Frequenza Cardiaca ===

frequenze = np.array([68, 65, 77, 110, 160, 161, 162, 161, 160, 161,
                      162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70])

min_freq = frequenze.min()
max_freq = frequenze.max()

esercizio = frequenze > 120
percentuale_esercizio = esercizio.sum() / len(frequenze) * 100

# === 5. Manipolazione stipendi ===

stipendi = np.array([50000, 105250, 55000, 89000], dtype=np.float64)
costo_iniziale = stipendi.sum()

# Aumento CEO
stipendi[stipendi == 105250] *= 1.15

# Verifica valore
valore_atteso = 105250 * 1.15
presente = valore_atteso in stipendi

# dtype per ottenere valore esatto
stipendi = np.array([50000, 105250, 55000, 89000], dtype=np.float64)
stipendi[stipendi == 105250] = 121037.5

# Aumento 20% per 50000
stipendi[stipendi == 50000] *= 1.2

# Aumento 10% per altri
maschera_altri = (stipendi != 121037.5) & (stipendi != 60000)
stipendi[maschera_altri] *= 1.1

# Nuovo costo totale
nuovo_costo = stipendi.sum()
costo_aumento_CEO = 121037.5 - 105250

# === 6. Valori di CO2 ===

co2 = np.array([16, 20, 19, 15, 18, 21, 17, 19])
sopra_soglia = co2[co2 > 18]
media_sopra = sopra_soglia.mean()
frazione_sopra = sopra_soglia.sum() / co2.sum()

# === 7. Analisi di una matrice ===

survey_matrix = np.array([
    [25, 40000, 10],
    [32, 52000, 12],
    [40, 63000, 14],
    [29, 47000, 11],
    [35, 58000, 13]
])

# Intervistati con almeno 12 anni di studio
filtrati = survey_matrix[survey_matrix[:, 2] >= 12]
redditi_filtrati = filtrati[:, 1]
reddito_medio = redditi_filtrati.mean()

# === 8. Rimpiazzare outliers ===

ages = np.array([92, 108, 75, 63, 62, 66, 90, 98, 97, 91, 86, 5,
                 98, 57, 96, 104, 96, 94, 72, 98, 111, 98, 89,
                 999, 67, 99, 85, 101, 70])

# Rimuovi outliers
ages_clean = ages[ages != 999]
massimo_valido = ages_clean.max()

# === 9. Generazione random di storie ===

lista_parole = [
    'INSIEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO',
    'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 'CERIMONIA',
    'ALFABETIZZAZIONE', 'CONSEGNA', 'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO',
    'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 'SCOPERTA',
    'PENALITÀ', 'VANTAGGIO', 'HOT DOG', 'ABITO', 'MATEMATICA', 'VARIANTE'
]

# Estrai 5 parole con reinserimento
scelte = random.choices(lista_parole, k=5)

# Inserisci nel testo
testo = (
    f"In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico {scelte[0]} che proteggeva.\n"
    f"Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il {scelte[1]} come dono,\n"
    f"i suoi occhi si spalancarono e lei esclamò una sola parola: \"{scelte[2]}\".\n"
    f"Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un {scelte[3]}.\n"
    f"Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.\n"
    f"Con un sorriso da un orecchio all'altro, e cantando canti di festa,\n"
    f"la donna saggia guardò i suoi compaesani e disse: \"Ora è giunto il tempo del banchetto – nessuno rimarrà mai più senza {scelte[4]}!\"\n"
    "Ci fu grande gioia e celebrazione."
)

print(testo)
