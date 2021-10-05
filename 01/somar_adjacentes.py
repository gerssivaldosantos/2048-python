""" Faça uma função que recebe uma lista de números e uma direção "d" ou "a"
caso a direcao seja "d", some os números adjacentes da esquerda para a direita,
caso seja "a", some da direita para a esquerda e retorne a lista somada 

Ex:
    somar_adjacentes([2,2,0,4,2],"d") -> [0,4,0,4,2]
    somar_adjacentes([2,2,0,4,2],"a") -> [4,0,0,4,2]
"""


def somar_adjacentes(linha, direcao):

    if direcao == "a":
        linha = linha[::-1]

    tam_linha = len(linha)
    aux = []
    excluidos = []
    ultimo = linha[-1:][0]

    # percorrendo do primeiro até o
    # penultimo número da linha

    for i in range(tam_linha - 1):

        if i not in excluidos:

            atual = linha[i]
            prox = linha[i + 1]

            if atual == prox:

                aux.append(0)
                aux.append(atual + prox)
                excluidos.append(i + 1)

            else:
                aux.append(atual)

    if len(aux) != tam_linha:
        aux.append(ultimo)

    if direcao == "a":
        aux = aux[::-1]

    return aux


somar_adjacentes([0, 2, 2, 0, 4, 4, 4], "a")
