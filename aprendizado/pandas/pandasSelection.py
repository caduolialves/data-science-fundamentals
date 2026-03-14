import pandas as pd

# Podemos adicionar um indice na laietura do arquivo, para alterar o indice padrão do DF para uma coluna específica.
# df_pokemon = pd.read_csv('data/pokemon.csv', index_col='Name')
df_pokemon = pd.read_csv('data/pokemon.csv')

#Precisando exibir todos os dados use o .to_string()


"""
Seleção por coluna
"""
# Exibe o nome das colunas do DataFrame
# print(df_pokemon.columns)

# Exibe a coluna que possui o mesmo nome que passar como argumento
# print(df_pokemon['Name'])

# Exibe uma lista de colunas a qual queremos exibir
# print(df_pokemon[['Name', 'Generation']])

"""
Seleção por linha
"""

# Seleciona a linha completa pelo indice
# print(df_pokemon.loc[0])

# Seleciona a linha apenas com as colunas que queremos exibir do indice ao 5
# print(df_pokemon.loc[0:5, ["Name", "Type 1", "Type 2"]])

# Seleciona a linha em um intervalo específico de indices e de colunas
#print(df_pokemon.iloc[0:5, 0:3])