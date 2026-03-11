import numpy as np

array = np.array([[1,2,3,4], 
                 [5,6,7,8], 
                 [9,10,11,12], 
                 [13,14,15,16]])

# array[start:end:step] seleção de linhas

#linha 0 até a linha 4, pulando de 2 em 2
print("Linha 0 até a linha 3, pulando de 2 em 2:")
print(array[0:3:2],"\n")

# inverte a ordem das linhas
print("Linhas em ordem inversa:")
print(array[::-1],"\n")

# array[:, start:end:step] seleção de colunas

#coluna 0 até a coluna 4, pulando de 2 em 2
print("Coluna 0 até a coluna 3, pulando de 2 em 2:")
print(array[:, 0:3:2],"\n")

# inverte a ordem das colunas
print("Colunas em ordem inversa:")
print(array[:, ::-1],"\n")

