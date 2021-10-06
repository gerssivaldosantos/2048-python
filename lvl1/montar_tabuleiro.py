""" Crie uma função que receba uma matriz númerica e retorna um tabuleiro
formatado para o número de algarismos contidos dentro do maior número contido
na matriz e substitua todos os zeros contidos na matiz por um espaço vazio 

Ex:
            --------------------------
            | 2  |    | 4  |256 |1024|
            --------------------------
            | 2  |    | 4  |    | 2  |
            --------------------------
            | 4  | 5  |    | 4  |    |
            --------------------------
"""


def maior_numero(matriz):
    """
    Recebe uma matriz númerica e retorna
    o maior número contido.

    list -> int"""
    maior = 0
    for linha in matriz:
        for coluna in linha:
            if coluna > maior:
                maior = coluna
    return maior


def montar_tabuleiro(matriz):

    # dimensões da matriz
    tam_linha = len(matriz)
    tam_coluna = len(matriz[0])

    m_num = maior_numero(matriz)
    espaço = len(str(m_num))
    
    print("-" * ((tam_coluna * espaço) + tam_coluna + 1))

    for linha in range(tam_linha):
        for coluna in range(tam_coluna):
            if matriz[linha][coluna] != 0:
                elemento = f"|{matriz[linha][coluna]:^{espaço}}"
            else:
                elemento = f"|{' ':^{espaço}}"
            print(elemento, end="")

        print("|")

        print("-" * ((tam_coluna * espaço) + tam_coluna + 1))


