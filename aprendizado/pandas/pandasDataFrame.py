import pandas as pd

data = {
  "nome": ["Cadu", "Luiza", "Maria"],
  "idade": [22, 25, 21]
}

def criar_data_frame(data_dict: dict, label_index: str | None = None):
    """
    Cria um DataFrame a partir de um dicionário, adicionando índices personalizados.

    Parametros
    ----------
    dict : dict
        Dicionário contendo os dados para criar o DataFrame.

    label_index : str, None
        Prefixo para os índices personalizados. Se None, o índice padrão será usado.

    Retorna
    -------
    pd.DataFrame
        O DataFrame criado a partir do dicionário, com índices personalizados se label_index for fornecido.
    """
    df = pd.DataFrame(data_dict)

    if label_index is None:
        return df

    df.index = [f"{label_index}{i}" for i in range(1, len(df)+1)]

    return df

def mostrar_data_frame(df: pd.DataFrame):
    print(df)

def adicionar_coluna(df: pd.DataFrame, nome_coluna: str, dados_coluna: list):
    """
    Adiciona uma nova coluna a um DataFrame existente.

    Parâmetros
    ----------
    df : pd.DataFrame
        O DataFrame ao qual a nova coluna será adicionada.
    nome_coluna : str
        O nome da nova coluna a ser adicionada.
    dados_coluna : list
        A lista de dados que será adicionada como a nova coluna. Deve ter o mesmo número de elementos que o número de linhas do DataFrame.
    
    Retorna
    -------
    pd.DataFrame
        O DataFrame atualizado com a nova coluna adicionada.
    """

    if len(dados_coluna) != len(df):
        raise ValueError("O número de elementos em dados_coluna deve ser igual ao número de linhas do DataFrame.")
    df[nome_coluna] = dados_coluna
    return df

def adicionar_linha(df: pd.DataFrame, dados_linha: dict, label_linha: str | None = None):
    """
    Adiciona uma nova linha a um DataFrame existente.

    Parâmetros
    ----------
    df : pd.DataFrame
        O DataFrame ao qual a nova linha será adicionada.
    dados_linha : dict
        O dicionário contendo os dados para a nova linha.
    label_linha : str | None, optional
        O rótulo para a nova linha. Se None, o índice padrão será usado.

    Retorna
    -------
    pd.DataFrame
        O DataFrame atualizado com a nova linha adicionada.
    """
    if label_linha is not None:
        df.loc[label_linha] = dados_linha
    else:
        df.loc[len(df)] = dados_linha
    return df

df = criar_data_frame(data, "pessoa")
mostrar_data_frame(df)
df = adicionar_coluna(df, "cidade", ["Vitória", "Três Passos", "Rio de Janeiro"])
mostrar_data_frame(df)
# Se remover a label_linha, a nova linha será adicionada com o índice numérico padrão (0, 1, 2, ...)
df = adicionar_linha(df, {"nome": "João", "idade": 30, "cidade": "São Paulo"}, "pessoa4")
mostrar_data_frame(df)