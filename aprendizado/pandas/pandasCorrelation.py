import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
A correlação, como o nome diz, mostra a correlação entre cada coluna
do dataset
"""

df = pd.read_csv('../../data/pokemon.csv')

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Matriz de Correlação")
plt.show()

# Com o plot dessa matriz de correlação conseguimos tirar boas ideias
# como por exemplo, fica claro que o Sp. Atk influencia bastante no 
# Total de atributos de cada Pokémon, assim como o Attack, também vemos
# que a geração não influencia em basicamente nada em qualquer tipo de 
# atributo de cada pokémon.