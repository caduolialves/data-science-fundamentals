import pandas as pd

# Uma série é uma estrutura de dados unidimensional, ou seja, é uma coluna de dados.

"""
Declaração de uma série:
"""

lista = [1, 7, 2]
lista2 = [4, 5, 6]
dicionario = {"a": 1, "b": 2, "c": 3}

def criar_serie(lista: list | dict, label: str | None = None) -> pd.Series:
    """
    Cria uma série a partir de uma lista com índices personalizados.

    Parâmetros
    ----------
    lista : list | dict
        A lista ou dicionário de dados que será convertido em uma série.

    label : str | None, optional
        O rótulo para personalizar os índices da série.

    Retorna
    -------
    pd.Series
        A série criada a partir da lista ou dicionário fornecido.
    """
    if label is None:
        serie = pd.Series(lista)
        return serie

    serie = pd.Series(lista, index=[label + "1", label + "2", label + "3"])
    return serie

serie = criar_serie(lista)
print("serie:\n", serie)
serie2 = criar_serie(lista2)

serie_com_indice_personalizado = criar_serie(lista, "num")
print("serie_com_indice_personalizado:\n", serie_com_indice_personalizado)

serie_com_dict = criar_serie(dicionario)
print("serie_com_dict:\n", serie_com_dict)



"""
Acessando os valores de uma série
"""
def acessar_valores_serie(serie: pd.Series, indice: int | str):
    """
    Acessa um valor específico em uma série usando o índice.

    Parâmetros
    ----------
    serie : pd.Series
        A série da qual o valor será acessado.

    indice : int | str
        O índice do valor a ser acessado. Pode ser um número inteiro ou uma string, dependendo do tipo de índice da série.

    Retorna
    -------
    Valor do índice especificado na série.
    """
    print(f"Valor do índice {indice}:", serie.loc[indice])


"""
Operações com séries
"""

# Filtrando valores maiores que 2
print("Filtro para valores maiores que 2:\n", serie[serie > 2], sep="")

# Somando duas séries com os mesmos índices
soma = serie + serie2
print("Soma de duas séries com os mesmos índices:\n", soma, sep="")

# Somando duas séries com indices diferentes:
# irá dar NaN para os índices que não existem em ambas as séries
# uma opção seria usar o .values para somar apenas os valores, ignorando os índices
soma_dif = serie + serie_com_dict
print("Soma de duas séries com indices de tipos diferentes:\n", soma_dif, sep="")
