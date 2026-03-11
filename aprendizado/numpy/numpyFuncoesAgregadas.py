import numpy as np

'''
Funções agregadas são funções que operam em um array e retornam um único valor, 
como a soma, média, mínimo, máximo, etc. Elas são usadas para resumir ou agregar
os dados de um array de forma eficiente.
'''

array = np.array([[1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 9]])

# Soma de todos os elementos do array
soma_total = np.sum(array)
print("Soma total:", soma_total)

# Média de todos os elementos do array
media_total = np.mean(array)
print("Média total:", media_total)

# Valor mínimo do array
minimo = np.min(array)
print("Valor mínimo:", minimo)

posicao_minimo = np.argmin(array)
print("Posição do valor mínimo (índice):", posicao_minimo)

# Valor máximo do array
maximo = np.max(array)
print("Valor máximo:", maximo)

# Soma dos elementos ao longo do eixo 0 (colunas)
soma_colunas = np.sum(array, axis=0)
print("Soma das colunas:", soma_colunas)

# Soma dos elementos ao longo do eixo 1 (linhas)
soma_linhas = np.sum(array, axis=1)
print("Soma das linhas:", soma_linhas)

# Desvio padrão dos elementos do array
desvio_padrao = np.std(array)
print("Desvio padrão:", desvio_padrao)

variancia = np.var(array)
print("Variância:", variancia)