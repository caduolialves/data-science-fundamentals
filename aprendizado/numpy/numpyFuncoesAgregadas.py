import numpy as np

"""
Funções agregadas são funções que operam em um array e retornam um único valor, 
como a soma, média, mínimo, máximo, etc. Elas são usadas para resumir ou agregar
os dados de um array de forma eficiente.
"""

array = np.array([[1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 9]])

def operacoes_agregadas(arr: np.ndarray):


    """
    Realiza operações agregadas em um array numpy.

    Parâmetros
    ----------
    arr : np.ndarray
        O array sobre o qual as operações agregadas serão realizadas.

    Retorna
    -------
    Soma total : float
        A soma de todos os elementos do array.

    Média total : float
        A média de todos os elementos do array.

    Valor mínimo : float
        O valor mínimo do array.

    Posição do valor mínimo (índice) : int
        A posição do valor mínimo no array, retornada como um índice.

    Valor máximo : float
        O valor máximo do array.

    Soma das colunas : np.ndarray
        A soma dos elementos ao longo do eixo 0 (colunas).

    Soma das linhas : np.ndarray
        A soma dos elementos ao longo do eixo 1 (linhas).

    Desvio padrão : float
        O desvio padrão dos elementos do array.

    Variância : float
        A variância dos elementos do array.
    """

    print("Soma total:", np.sum(arr))
    print("Média total:", np.mean(arr))
    print("Valor mínimo:", np.min(arr))
    print("Posição do valor mínimo (índice):", np.argmin(arr))
    print("Valor máximo:", np.max(arr))
    print("Soma das colunas:", np.sum(arr, axis=0))
    print("Soma das linhas:", np.sum(arr, axis=1))
    print("Desvio padrão:", np.std(arr))
    print("Variância:", np.var(arr))

operacoes_agregadas(array)

