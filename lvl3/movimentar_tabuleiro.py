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

def movimentar_tabuleiro(tabuleiro, direcao):
    """ Recebe direções "a,w,s,d", e move os números no tabulerio 
    list -> list"""
    aux = []
    if direcao == "d":
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha,"a")
            aux.append(nova_linha)
    elif direcao == "a":
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha,"d")
            aux.append(nova_linha)
    elif direcao == "s":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha,"a")   
            aux.append(nova_linha)
        
        aux = transpor_matriz(aux)
    elif direcao == "w":
        tabuleiro = transpor_matriz(tabuleiro)
        for linha in tabuleiro:
            nova_linha = mover_zeros(linha,"d")  
            aux.append(nova_linha)
        aux = transpor_matriz(aux)
    
    return aux