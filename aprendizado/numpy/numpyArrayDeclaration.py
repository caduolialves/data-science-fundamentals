import numpy as np

lista_comum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

'''
O array no numpy é uma estrutura chamada ndarray (n-dimensional array), que é
uma coleção de elementos do mesmo tipo, organizados em uma grade de dimensões.
Ele é a estrutura de dados fundamental do numpy e é usado para armazenar e manipular grandes 
conjuntos de dados numéricos de forma eficiente, sendo 50x mais rápido que listas do Python.
'''


# Array e suas dimensionalidades

# Quando declaramos um array com apenas um elemento, ele é chamado de 0-D Array, sem dimensões ou eixos.
array_0d = np.array(5)

print("\nArray 0D:")
print(array_0d)
print("Shape: (numero_de_linhas, numero_de_colunas)", array_0d.shape)
print("Dimensions:", array_0d.ndim)
print("Size:", array_0d.size)
print("Data Type:", array_0d.dtype)

# Já um array 1-D é um array unidimensional, ou seja, uma sequência de elementos organizados em uma única linha ou coluna.

lista_numpy = np.array([0,1,2,3,4,5])

print("Array 1D:")
print(lista_numpy)
print("Shape: (numero_de_linhas, numero_de_colunas)", lista_numpy.shape)
print("Dimensions:", lista_numpy.ndim)
print("Size:", lista_numpy.size)
print("Data Type:", lista_numpy.dtype)

'''
Agora quando falamos em um array 2 - D, estamos falando de uma matriz, ou seja,
um array com duas dimensões, onde os elementos estão organizados em linhas e colunas.
'''
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])

print("\nArray 2D:")
print(array_2d)
print("Shape: (numero_de_linhas, numero_de_colunas)", array_2d.shape)
print("Dimensions:", array_2d.ndim)
print("Size:", array_2d.size)
print("Data Type:", array_2d.dtype)

'''
Já um array 3 - D é um array tridimensional, onde os elementos estão organizados em camadas,
linhas e colunas. Ele é usado para representar dados que possuem uma estrutura mais complexa, como imagens ou volumes.
'''

array_3d = np.array([[[1, 2], [3, 4]], 
                     [[5, 6], [7, 8]]])

print("\nArray 3D:")
print(array_3d)
print("Shape: (numero_de_linhas, numero_de_colunas)", array_3d.shape)
print("Dimensions:", array_3d.ndim)
print("Size:", array_3d.size)
print("Data Type:", array_3d.dtype)

'''
Caso você queria adicionar mais numeros de dimensão, é só adicionar o argument ndmin na delaração do array,
como por exemplo: arr = np.array([1, 2, 3, 4], ndmin=5)
'''
