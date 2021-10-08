""" Quando o jogo 2048 é inicializado, ele cria um tabuleiro onde todos os elementos
são vazios exceto 2. Seguindo esse raciocı́nio, crie uma função que crie uma matriz
de zeros n por n, exceto em duas posições aleatórias que devem conter o número 2.
O valor default de n deve ser 4. """

from random import randint

#Declaração da função com valor 4 como defaul de "n"
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