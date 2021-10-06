
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

def achar_adjacentes(tabuleiro):
    len_linha = len(tabuleiro)
    len_coluna = len(tabuleiro[0])
    achar_adjacentes = 0
    rotacoes = 0
    while rotacoes < 6:
        aux = []
        for linha in tabuleiro:
            aux.append(mover_zeros(linha,"d"))

        for linha in range(len_linha):
            for coluna in range(len_coluna -1):
                prox = aux[linha][coluna + 1]
                atual = aux[linha][coluna]
                if prox == atual and prox != 0 and atual != 0:
                    return True
                   

        tabuleiro= transpor_matriz(tabuleiro)

        rotacoes += 1
    return False
                
def status_tabuleiro(tabuleiro,maximo):
    #Guia de retornos:
    #o retorno é uma lista com 3 posições, sendo o zero na posição
    #indicando um "Sim" e o 1, "Não"
    #Primeiro elemento da lista: O número máximo foi atingido ?
    #Segundo elemento da lista: Existem números zeros no tabuleiro
    #Terceiro elemento da lista: Existem jogadas possiveis?

    cont_maximo = 0
    cont_zeros = 0
    len_linha = len(tabuleiro)
    len_coluna = len(tabuleiro[0])

    for linha in tabuleiro:
        for coluna in linha:
            if coluna == maximo:
                cont_maximo += 1
            if coluna == 0:
                cont_zeros += 1
    retorno = []
    if cont_maximo > 0:
        retorno.append(0)
    else:
        retorno.append(1)
    if cont_zeros > 0:
        retorno.append(0)
    else:
        retorno.append(1)
    if achar_adjacentes(tabuleiro):
        retorno.append(0)
    else:
        retorno.append(1)
    return retorno
    

                     