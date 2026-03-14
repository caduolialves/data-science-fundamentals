import pandas as pd

df = pd.read_csv('data/pokemon.csv')

"""
Filtragem de dados
"""

# Criar um dataframe apenas com os pokemons do tipo fogo que não possuem um segundo tipo

def criar_dataframe_com_filtro(type1: str, type2: str | None = None):


    if type1 == df['Type 2']:
        df_tipos = df[
            (df['Type 1'] == type1) |
            (df['Type 2'] == type1)
        ]

    elif type2 is None:
        df_tipos = df[
            (df['Type 1'] == type1) &
            (df['Type 2'].isna())
        ]

    else:
        df_tipos = df[
            (df['Type 1'] == type1) &
            (df['Type 2'] == type2)
        ]

    return df_tipos

df_fogo = criar_dataframe_com_filtro('Fire')
print(df_fogo)

# df_fogo_e_veneno = criar_dataframe_com_filtro('Fire', 'Poison')
# print(df_fogo_e_veneno)

# df_fogo_e_agua = criar_dataframe_com_filtro('Fire', 'Water')
# print(df_fogo_e_agua)

"""
Ordenação dos dados
"""

# print(df.sort_values(by='HP', ascending=False))

# print(df.sort_values(by='Attack', ascending=False))

# print(df.sort_values(by='Total', ascending=False))

