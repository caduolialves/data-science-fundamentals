import numpy as np

"""
Filtragem de dados é o processo de selecionar um subconjunto de dados com base em condições específicas.
"""

array = np.array([[1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 9]])

# Filtrar elementos maiores que 5
filtro_maior_5 = array > 5
print("Filtro para elementos maiores que 5:\n", filtro_maior_5)

elementos_maior_5 = array[filtro_maior_5]
print("Elementos maiores que 5:", elementos_maior_5)

# Filtrar elementos pares
filtro_pares = array % 2 == 0

elementos_pares = array[filtro_pares]
print("Elementos pares:", elementos_pares)

# Criando um array com elementos ímpares divisiveis por 3 com np.where
impares = np.where((array % 2 == 1) & (array % 3 == 0), array, 0)
print("Elementos ímpares:", impares)