import numpy as np

def criar_e_mostrar_array(dados, ndmin: int | None = None):
    """
    Cria um ndarray numpy e imprime suas propriedades.

    Parâmetros
    ----------
    dados : qualquer estrutura iterável ou valor
        Dados usados para criar o array.

    ndmin : int | None
        Número mínimo de dimensões do array.

    Retorna
    -------
    np.ndarray
        O array criado.
    """

    if ndmin is not None:
        arr = np.array(dados, ndmin=ndmin)
    else:
        arr = np.array(dados)

    return arr

def mostrar_propriedades_array(arr: np.ndarray):

    """
    Imprime as propriedades de um array numpy.

    Parâmetros
    ----------
    arr : np.ndarray
        O array cujas propriedades serão exibidas.

    Retorna
    -------
    Array : np.ndarray
        O array cujas propriedades estão sendo exibidas.

    Shape : tupla
        A forma do array, indicando o número de elementos em cada dimensão.
    
    Dimensions : int
        O número de dimensões do array.
    
    Size : int
        O número total de elementos no array.
    
    Data Type : dtype
        O tipo de dados dos elementos no array.
    """
    print("Array:\n", arr, sep="")
    print("Shape:", arr.shape)
    print("Dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Data Type:", arr.dtype)
    print("----------")

dados = [1, 2, 3, 4, 5]
array = criar_e_mostrar_array(dados)
mostrar_propriedades_array(array)

dados = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
array = criar_e_mostrar_array(dados)
mostrar_propriedades_array(array)