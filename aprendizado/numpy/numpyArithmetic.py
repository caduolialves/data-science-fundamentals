import numpy as np

# Aritimética escalar(escalar = unico valor) 
array = np.array([1.2, 2.5, 3.0, 4.01])

raios = np.array([1.0, 2.0, 3.0, 4.0])
PI = np.pi

print("Array original:", array)

print("array + 1:", array + 1)  # Adiciona 1 a cada elemento do array
print("array - 1:", array - 1)  # Subtrai 1 de cada elemento do array
print("array * 2:", array * 2)  # Multiplica cada elemento do array por 2
print("array / 2:", array / 2)  # Divide cada elemento do array por 2
print("array ** 2:", array ** 2) # Eleva cada elemento do array ao quadrado

#Funções matemáticas vetorizadas
print("np.sqrt(array):", np.sqrt(array))  # Calcula a raiz quadrada de cada elemento do array
print("np.sin(array):", np.sin(array))   # Calcula o seno de cada elemento do array
print("np.cos(array):", np.cos(array))   # Calcula o cosseno de cada elemento do array
print("np.round(array):", np.round(array))   # Arredonda cada elemento do array
print("np.floor(array):", np.floor(array)) # Arredonda cada elemento do array para baixo
print("np.ceil(array):", np.ceil(array)) # Arredonda cada elemento do array para cima
print("np.pi:", np.pi) # Retorna o valor de π

# Calculando a área de um círculo usando a fórmula A = π * r^2
areas = PI * raios ** 2
print("Áreas dos círculos:", areas)

# Operações entre arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("array1 + array2:", array1 + array2)  # Soma elemento a elemento
print("array1 - array2:", array1 - array2)  # Subtração elemento a elemento
print("array1 * array2:", array1 * array2)  # Multiplicação elemento a elemento
print("array1 / array2:", array1 / array2)  # Divisão elemento a elemento
print("array1 ** array2:", array1 ** array2) # Eleva cada elemento de array1 à potência do elemento correspondente em array2

# Operadores de comparação
print("array1 == array2:", array1 == array2)  # Verifica se os elementos são iguais
print("array1 != array2:", array1 != array2)  # Verifica se os elementos são diferentes
print("array1 > array2:", array1 > array2)    # Verifica se os elementos de array1 são maiores que os de array2
print("array1 < array2:", array1 < array2)    # Verifica se os elementos de array1 são menores que os de array2 