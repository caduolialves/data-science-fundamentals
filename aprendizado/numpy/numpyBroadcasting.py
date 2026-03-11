import numpy as np

'''
broadcasting é um conjunto de regras para aplicar operações entre arrays de diferentes formas.
Ele permite que operações sejam realizadas em arrays de tamanhos diferentes, desde que sejam compatíveis em termos de forma.

As dimensões devem ser iguais ou uma das dimensões deve ser 1 para que o broadcasting funcione.
EX: a(4x3) + b(1x3) = (4x3)
'''

# Exemplo 1: Adição de um escalar a um array
array1 = np.array([[1, 2, 3, 4, 5]])
array2 = np.array([[1], [2], [3], [4], [5]])

print(array1.shape)
print(array2.shape)
print(array1 * array2)
