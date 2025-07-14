
# Lezione 1 



#  1. Trasformare cicli in list comprehension 

# Esempio 1: quadrati dei numeri da 0 a 4
lista1 = []
for i in range(5):
    lista1.append(i**2)

# List comprehension equivalente
lista1_comp = [i**2 for i in range(5)]

# Esempio 2: caratteri maiuscoli
lista2 = []
for char in 'ciao':
    lista2.append(char.upper())

# List comprehension equivalente
lista2_comp = [char.upper() for char in 'ciao']

# Esempio 3: numeri pari
lista3 = []
for n in range(10):
    if n % 2 == 0:
        lista3.append(n)

# List comprehension equivalente
lista3_comp = [n for n in range(10) if n % 2 == 0]

# 2. Vettore di Numeri Primi 

import numpy as np

# 1. Crea un vettore di numeri primi tra 0 e 10
primi = np.array([2, 3, 5, 7])

# 2. Conta quanti numeri ci sono
print("Numero di elementi (len):", len(primi))
print("Numero di elementi (.size):", primi.size)

# 3. Tipo di dato (dtype)
print("Tipo di dato:", primi.dtype)

# 4. Usando list comprehension per generare array di numeri primi
primi_lc = np.array([x for x in range(11) if all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1])
print("Numeri primi generati con list comprehension:", primi_lc)

# === 3. Operazioni su array ===

# Array a
a = np.array([1, 2, 3, 4, 5])

# b: sottostringa
b = a[1:4]  # [2, 3, 4]

# c: reverse dell’array a
c = a[::-1]  # [5, 4, 3, 2, 1]

# Divisione di a con c
a_div = a / c  # elemento per elemento

# Stessa cosa con una lista normale
lista = [1, 2, 3, 4, 5]
b_lista = lista[1:4]
c_lista = lista[::-1]
a_div_lista = [x / y for x, y in zip(lista, c_lista)]

# Stampa dei risultati
print("Array a:", a)
print("Array b:", b)
print("Array c (reverse):", c)
print("Divisione a / c:", a_div)

print("Lista originale:", lista)
print("Lista b:", b_lista)
print("Lista c (reverse):", c_lista)
print("Divisione lista:", a_div_lista)
