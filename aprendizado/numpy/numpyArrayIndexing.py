import numpy as np

"""
A indexação de arrays é equivalente ao acesso a um elemento de um array.
Você pode acessar um elemento de um array referenciando seu número de índice.
Os índices em arrays NumPy começam com 0, o que significa que o primeiro
elemento tem índice 0, o segundo tem índice 1 e assim por diante.
"""
array = np.array([1, 2, 3, 4])

array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])

array_3d = np.array([[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
                     [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]],
                     [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "_"]]])

def mostrar_array_1_D(arr: np.ndarray):
    """
    Imprime os elementos de um array 1-D.

    Parâmetros
    ----------
    arr : np.ndarray
        O array 1-D cujos elementos serão exibidos.

    Retorna
    -------
    Array : np.ndarray
        O array 1-D cujos elementos estão sendo exibidos.
    
    array[0] : elemento
        O primeiro elemento do array 1-D.

    array[1] : elemento
        O segundo elemento do array 1-D.
    
    array[2] + array[3] : elemento
        A soma do terceiro e quarto elemento do array 1-D.
    """
    print("Array 1-D:", arr)
    print("array[0]:", array[0])
    print("array[1]:", array[1])
    print("array[2] + array[3]:", array[2] + array[3])


def mostrar_array_2_D(arr: np.ndarray):
    """
    Imprime os elementos de um array 2-D.

    Parâmetros
    ----------
    arr : np.ndarray
        O array 2-D cujos elementos serão exibidos.

    Retorna
    -------
    Array : np.ndarray
        O array 2-D cujos elementos estão sendo exibidos.
    
    array[0, 0] : elemento
        O primeiro elemento do array 2-D.

    array[1, 0] : elemento
        O segundo elemento do array 2-D.
    
    array[2, 0] + array[3, 0] : elemento
        A soma do terceiro e quarto elemento do array 2-D.
    """
    print("Array 2-D:", arr)
    print("array[0, 0]:", array[0, 0])
    print("array[1, 0]:", array[1, 0])
    print("array[2, 0] + array[3, 0]:", array[2, 0] + array[3, 0])


def mostrar_array_3_D(arr: np.ndarray):
    """
    Imprime os elementos de um array 3-D.

    Parâmetros
    ----------
    arr : np.ndarray
        O array 3-D cujos elementos serão exibidos.

    Retorna
    -------
    Array : np.ndarray
        O array 3-D cujos elementos estão sendo exibidos.
    
    array[0, 0, 0] : elemento
        O primeiro elemento do array 3-D.

    array[1, 0, 0] : elemento
        O segundo elemento do array 3-D.
    
    array[2, 0, 0] + array[3, 0, 0] : elemento
        A soma do terceiro e quarto elemento do array 3-D.
    """
    print("Array 3-D:", arr)
    print("array[0, 0, 0]:", array[0, 0, 0])
    print("array[1, 0, 0]:", array[1, 0, 0])
    print("array[2, 0, 0] + array[3, 0, 0]:", array[2, 0, 0] + array[3, 0, 0])

mostrar_array_1_D(array)
mostrar_array_2_D(array_2d)
mostrar_array_3_D(array_3d)