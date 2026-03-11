import numpy as np

'''
A indexação de arrays é equivalente ao acesso a um elemento de um array.
Você pode acessar um elemento de um array referenciando seu número de índice.
Os índices em arrays NumPy começam com 0, o que significa que o primeiro
elemento tem índice 0, o segundo tem índice 1 e assim por diante.
'''
array = np.array([1, 2, 3, 4])

# print do array 1-D
print("array:", array)
# printando o primeiro elemento do array
print("array[0]:", array[0])
# printando o segundo elemento do array
print("array[1]:", array[1])
# printando o terceiro e quarto elemento do array e somando-os
print("array[2] + array[3]:", array[2] + array[3])

# Acessando elementos de um array 2D
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])

# print do array 2-D
print("\narray_2d:\n", array_2d)

# printando o elemento da primeira linha e primeira coluna
print("array_2d[0, 0]:", array_2d[0, 0]) 

# printando o elemento da segunda linha e primeira coluna
print("array_2d[1, 0]:", array_2d[1, 0])

# usando indices negativos para acessar o último elemento da primeira linha
print("array_2d[0, -1]:", array_2d[0, -1])

 # Acessando elementos de um array 3D
array_3d = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
                     [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]],
                     [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "_"]]])
print("\narray_3d:\n", array_3d)

# Visualização do shape do array 3D
print("Shape do array_3d:", array_3d.shape)

# printando meu apelido com um array 3 - D, Cadu.
print("Mey apelido é:" , array_3d[0,0,2] + array_3d[0,0,0] + array_3d[0,1,0] + array_3d[2,0,2])