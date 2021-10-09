def somar_adjacentes(linha, direcao):

    if direcao == "a":
        linha = linha[::-1]

    tam_linha = len(linha)
    aux = []
    excluidos = []
    ultimo = linha[-1:][0]
    score = 0

    # percorrendo do primeiro até o
    # penultimo número da linha

    for i in range(tam_linha - 1):

        if i not in excluidos:

            atual = linha[i]
            prox = linha[i + 1]
            if atual == prox:
                aux.append(0)
                aux.append(atual + prox)
                score += atual + prox
                excluidos.append(i + 1)
            else:
                aux.append(atual)
    if len(aux) != tam_linha:
        aux.append(ultimo)

    if direcao == "a":
        aux = aux[::-1]

    return aux, score

def mover_zeros(linha, direcao):
    zeros = []
    outros = []

    for numero in linha:
        #separando
        if numero == 0:
            zeros.append(numero)
        else:
            outros.append(numero)

    #unindo de acordo à direcao desejada
    if direcao == "d":
        return outros + zeros
    elif direcao == "a":
        return zeros + outros

def transpor_matriz(matriz):
    #extraindo tamanho da matriz
    len_lin = len(matriz)
    len_col = len(matriz[0])
    matriz_transposta = []

    #Criando uma matriz auxiliar
    #com as dimensões da transposta 
    for linha in range(len_col):
        nova_linha = []
        for coluna in range(len_lin):
            nova_linha.append(None)
        matriz_transposta.append(nova_linha)
    
    #Percorrendo a matriz original e alocando 
    #Os dados na transposta
    for linha in range(len_lin):
        for coluna in range(len_col):
            matriz_transposta[coluna][linha] = matriz[linha][coluna]

    return matriz_transposta

def somar_tabuleiro(tabuleiro, direcao):
    """ Recebe direções "a,w,s,d", e move os números no tabulerio 
    list -> list"""
    aux = []
    score = 0
    if direcao == "d":
        for linha in tabuleiro:
            nova_linha = somar_adjacentes(linha,"d")[0]
            score += somar_adjacentes(linha,"d")[1]
            aux.append(nova_linha)
    elif direcao == "a":
        for linha in tabuleiro:
            nova_linha = somar_adjacentes(linha,"a")[0]
            score += somar_adjacentes(linha,"a")[1]
            aux.append(nova_linha)
    elif direcao == "s":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = somar_adjacentes(linha,"d")[0]
            score += somar_adjacentes(linha,"d")[1]
            aux.append(nova_linha)
        
        aux = transpor_matriz(aux)
    elif direcao == "w":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = somar_adjacentes(linha,"a")[0]
            score += somar_adjacentes(linha,"a")[1]
            aux.append(nova_linha)
        aux = transpor_matriz(aux)
    
    return aux,score

def status_tabuleiro(tabuleiro):
    """ Recebe uma matriz e retorna True caso ainda existam 
    jogadas possíveis e False caso não existam
     """
    movimentos = ["w","a","s","d"]
    for linha in tabuleiro:
        for numero in linha:
            if numero == 0:
                return True
    tabuleiro_antigo = tabuleiro
    for movimento in movimentos:
        tabuleiro = somar_tabuleiro(tabuleiro,movimento)[0]

        if tabuleiro != tabuleiro_antigo:
            return True
    return False

""" print(status_tabuleiro(
    [[8, 2, 8], 
     [4, 8, 2], 
     [1, 8, 4]])) """

