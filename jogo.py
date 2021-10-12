from random import choice
from random import randint

def mensagem():

    print("""
                        :'#######::::'#####:::'##:::::::::'#######::
                        '##.... ##::'##.. ##:: ##:::'##::'##.... ##:
                        ..::::: ##:'##:::: ##: ##::: ##:: ##:::: ##:
                        :'#######:: ##:::: ##: ##::: ##::: #######::
                        '##:::::::: ##:::: ##: #########:'##.... ##:
                        ##::::::::. ##:: ##::...... ##:: ##:::: ##:
                        #########::. #####::::::::: ##::. #######::
                        .........::::.....::::::::::..::::.......:::
                                    Seja bem vindo(a)!
""")
    print(""" 
                                        Como jogar ? 
    
    Ao começar o jogo, um tabuleiro será criado, nele existirá números que são pontencia de 2,
ao mover as setas (w,s,a,d) você pode indicar as direções para cima (w) para baixo (s) para
direita (d) e para esquerda (a), ao fazer isso, os números que estiverem em linhas adjascentes 
na direção que você escolheu e forem iguais serão somados. A cada movimentação, 1 novo valor é inserido
no tabuleiro.

        O objetivo do jogo é mover o tabuleiro de forma que a organização fique a cada vez mais propicia a
soma de todos os números do tabuleiro, porque caso ele se encha e não seja mais possivel a soma por movimentação
o jogo acaba. Então tente fazer o máximo de movimentos possiveis antes disso acontecer !!
Boa Sorte ! 
    """)

def gerar_tabuleiro(n = 4):
    matriz = []
    while True:
        #Sorteando as posições onde será preenchido
        posicao1 = [randint(0,n - 1),randint(0,n - 1)]
        posicao2 = [randint(0,n - 1),randint(0,n - 1)]
        #Garantindo que as posições sorteadas não sejam iguais
        if posicao1 != posicao2:
            break
    
    #percorrendo a matriz e alocando os números nas posições 
    #sorteadas
    for linhas in range(n):
        linha = []
        for colunas in range(n):
            if [linhas,colunas] == posicao1 or [linhas,colunas] == posicao2:
               
                linha.append(2)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def gerar_aleatorio(matriz):
    #extraindo o tamanho da matriz para percorre-la

    len_lin = len(matriz)
    len_col = len(matriz[0])

    #extraindo as posicoes dos numeros zeros

    zeros_posi = []
    for linha in range(len_lin):
        for coluna in range(len_col):
            if matriz[linha][coluna] == 0:
                zeros_posi.append((linha,coluna))

    #Escolhendo qual dos zeros substituir 
    zero_sorteado = choice(zeros_posi)
   
    #Fazendo com que o 2 seja mais provavel de ser 
    #escolhido como substituto
    substitutos = (2,2,4)
    substituto = choice(substitutos)

    #Substituindo
    matriz[zero_sorteado[0]][zero_sorteado[1]] = substituto

    return matriz

def receber_jogada():
    """ Lê uma jogada e confere se ela é válida """
    #Lista com as jogadas válidas
    validas = ["a","s","d","w"]
    while True:
        #Conferindo se a jogada faz parte do conjunto
        #de válidas
        jogada = input("""\n  W \nA S D :""")
        if jogada.lower() in validas:
            return jogada.lower()
        else:
            print(f'\n"{jogada}" não é uma jogada válida. ')

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
    """ Recebe uma lista númerica e uma direcao, retorna
    uma cópia onde todos os zeros são movidos para a direção 
    dada como entrada
    
    list -> list
     """
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
    """ Recebe uma matriz e retorna a sua transposta
    list -> list """
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
    """ Recebe um tabuleiro e direções "a,w,s,d", soma números 
    adjacentes na direcao indicada na entrada e incrementa um 
    score com o resultado da soma dos números, é retonado o
    tabuleiro somado e o score
    list -> tuple"""
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
    list -> bool
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

def movimentar_tabuleiro(tabuleiro, direcao):
    """ Recebe direções "a,w,s,d", e move os números no tabuleiro 
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
    """ Recebe uma matriz e printa em formatação
    de tabela
    list -> None """
    # dimensões da matriz
    tam_linha = len(matriz)
    tam_coluna = len(matriz[0])

    m_num = maior_numero(matriz)
    espaço = len(str(m_num)) + 2
    
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

def main():
    #Exibindo Banner do jogo gerado em figlet
    #Escrevendo regras na tela
    mensagem()
    #Iniciando o record
    scores = []
    record = 0
    ficar_menu = True
    while ficar_menu:
        opcao = input("\n[ 0 ]Começar uma nova partida\n[ 1 ] Exibir Record e Histórico de partidas\n[ 2 ] Sair do jogo Opção: ")
        if opcao == "0":
            menu_tamanho = True
            while menu_tamanho:
                tamanhos_validos = ["3","4","5","6","7","8","9"]
                tamanho = str(input("""\nEscolha um tamanho de tabuleiro (3 - 9)\nTamanho :"""))       
                if tamanho in tamanhos_validos:
                    tamanho = int(tamanho)
                    menu_tamanho = False
                else:
                    print("\nTamanho inválido.\n")

            #Gerando e montando o tabuleiro
            tabuleiro = gerar_tabuleiro(n=tamanho)
            #Inicializando o Score do jogo
            score = 0
            #Montagem inicial do tabuleiro
            montar_tabuleiro(tabuleiro)
            status = True
            while status:
                #Recebendo, validando e recebendo como retorno a jogada
                #do usuário
                print(f"                   Score: [{score}]")
                #Recebendo jogada do usuário
                jogada = receber_jogada()
                #Movendo os números do tabuleiro
                tabuleiro = movimentar_tabuleiro(tabuleiro,jogada)
                #Somando os adjacentes na direcao indicada
                somado = somar_tabuleiro(tabuleiro,jogada)
                tabuleiro = somado[0]
                score += somado[1]
                status = status_tabuleiro(tabuleiro)
                if status == True:
                    zeros = 0
                    for linha in tabuleiro:
                        for coluna in linha:
                            if coluna == 0:
                                zeros += 1
                    if zeros > 0:
                        tabuleiro = gerar_aleatorio(tabuleiro)
                    montar_tabuleiro(tabuleiro)
                else:
                    if score > record:
                        record = score

                    scores.append([tamanho,score])
                    
                    print(f"\nGame Over ! Score: {score}\n")
        elif opcao == "1":
            if len(scores) == 0:
                print("\nAinda não houveram jogadas !\n")
            else:    
                print(f"\nMelhor jogada até agora :{record}\n")
                print("Lista com todos os scores até agora:")
                print("\n-----------\n|Tam |Score")
                montar_tabuleiro(scores)
        elif opcao == "2":
            print("\nJogo Finalizado ! Até mais !\n")
            ficar_menu = False
        else:
            print("\nEntrada inválida, tente novamente ! \n")
                
main()