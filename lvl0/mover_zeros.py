""" Crie uma função que receba uma lista númerica e os parametros "d" e "a",
caso o segundo parametro seja "d", mova todos os zeros contidos na lista para
a direita, caso seja "a", mova-os para a esquerda.

Adendo:
    "d" e "a" seguindo a lógica
das setas "wasd" usadas com a mão esquerda para jogar, se não tem familiaridade
pesquisa a respeito. """

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
    
    

