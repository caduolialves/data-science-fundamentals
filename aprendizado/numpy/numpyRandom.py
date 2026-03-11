import numpy as np

'''
O módulo numpy.random é uma subbiblioteca do NumPy que fornece funções para gerar números aleatórios
e realizar operações relacionadas a aleatoriedade. Ele é amplamente utilizado em ciência de dados, 
simulações, machine learning e outras áreas onde a geração de dados aleatórios é necessária.

Documentação: https://numpy.org/devdocs/reference/random/index.html
'''

# Se quiser usar os mesmos numeros aleatórios para fins de reprodução, você pode definir uma semente (seed) Ex: rng = np.random.default_rng(seed=1)
rng = np.random.default_rng()

# Rodar um dado de 6 lados
# size=1 significa que queremos gerar um único número aleatório
dado = rng.integers(low=1, high=7, size=1)
print("Resultado do dado:", dado)