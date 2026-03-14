import pandas as pd

"""
Limpeza de dados é o processo de identificar e corrigir ou remover dados incorretos,
incompletos, irrelevantes ou mal formatados em um conjunto de dados.
O objetivo da limpeza de dados é melhorar a qualidade dos dados para análise,
garantindo que os resultados sejam precisos e confiáveis.
"""
df = pd.read_csv('data/pokemon.csv')

# Remover colunas desnecessárias
# df = df.drop(columns=["#","Name"])

"""
Trabalhando com células vazias:
"""

# Para substituir valores ausentes por um valor específico, podemos
# usar o método fillna().
# df.fillna("None", inplace = True)

# Substituir valores ausentes por None da coluna "Type 2"
# df = df.fillna({"Type 2": "None"})


"""
---------------------------
"""

# Caso o data set seja muito grande, podemos usar o método dropna()
# para remover linhas com valores ausentes, sem ter grandes impactos
# na análise.
# new_df = df.dropna()

# O dropna() retona um novo DataFrame, mantendo o DataFrame original
# inalterado. Se quisermos modificar o DataFrame original, podemos
# usar o parâmetro inplace=True:
# df.dropna(inplace=True)

"""
---------------------------
"""

# Uma forma comum de substituir valores ausentes é usando a média,
# mediana ou moda da coluna. Por exemplo, para substituir valores
# ausentes na coluna "Attack" pela média:

# media = df["Attack"].mean()
# mediana = df["Attack"].median()
# moda = df["Attack"].mode()[0]
# df["Attack"].fillna(media, inplace=True)

"""
Trabalhando com dados com formatação incorreta:
"""

# Para tal situação, temos duas opções: remover as linhas ou converter
# todas as células das colunas para o mesmo formato.

# Podemos por exemplo, converter todos os nomes para maiúsculas usando
# o método str.upper():
# df["Name"] = df["Name"].str.upper()

"""
---------------------------
"""

# Para remover linhas com formatação incorreta, podemos usar o método
# drop() ou dropna() dependendo do caso. Por exemplo, para remover linhas
# onde a coluna "Type 1" tem um valor incorreto:

# Cria um array com os tipos válidos, removendo os valores ausentes e
# mantendo apenas os valores únicos.
# tipos_validos = df["Type 1"].dropna().unique()

# Em seguida, podemos usar o método isin() para filtrar o DataFrame e
# manter apenas as linhas onde "Type 1" tem um valor presente no array
# de tipos válidos:
# df = df[df["Type 1"].isin(tipos_validos)]


"""
---------------------------
"""

# Nós podemos usar o plotbox de qualquer coluna quantitativa, o ataque por
# exemplo.

# df["Attack"].plot.box()

# Ao executarmos o trecho acima, veremos um bloxpot, mostrando alguns pontos
# isolados, que são chamados de outliers. O quadrado central representa a 
# concentração de 50% dos dados. A linha verde significa a mediana e as linhas
# os limites sem os outliers

# Nós podemos coletar diversas informações de uma coluna com o seguinte comando:

# df["Attack"].describe()

# com ele, temos o resultado:

# count    800.000000
# mean      79.001250
# std       32.457366
# min        5.000000
# 25%       55.000000
# 50%       75.000000
# 75%      100.000000
# max      190.000000
# Name: Attack, dtype: float64

# A formula matemática utilizada para calcular os outliers usa de algumas
# variáveis deste resultado.

# IQR = Q3(75%) - Q1(25%)
# No nosso caso:
# IQR = 100 - 55
# IQR = 45

# Em sequida, definimos o limite superior e inferior:
# limite superior = Q3 + (1.5 × IQR)
# limite superior = 100 + (1.5 x 45)
# limite superior = 167.5

# limite inferior = Q1 - (1.5 × IQR)
# limite inferior = 55 - (1.5 x IQR)
# limite inferior = - 12.5

# Com isso podemos identificar nossos outliers.

# limite_superior = 167.5
# limite_inferior = -12.5

# outliers = df[(df["Attack"]>limite_superior) | (df["Attack"]<limite_inferior)]

# Desta forma, percebemos que todos os pokémons outliers são Mega Evoluções
# Caso o outlier seja um dado incorreto, podemos decidir se vamos manter,
# apagar ou corrigir. Nesse nosso caso vamos manter.