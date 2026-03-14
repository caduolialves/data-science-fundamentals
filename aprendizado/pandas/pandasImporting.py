import pandas as pd

df = pd.read_json('data/trending_repositories.json')
df_pokemon = pd.read_csv('data/pokemon.csv')

# Exibe os 5 primeiros e 5 ultimos registros do DataFrame
print(df_pokemon)

# Exibe todos os registros do DataFrame
# print(df_pokemon.to_string())

