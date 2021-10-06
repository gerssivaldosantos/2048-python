from random import choice

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
