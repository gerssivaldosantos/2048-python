#Modulos feitos até agora e em ordem cronológica

#level 0
from lvl0.mover_zeros import mover_zeros
from lvl0.receber_jogada import receber_jogada
from lvl0.somar_adjacentes import somar_adjacentes
from lvl0.menu import menu
#level 1
from lvl1.gerar_aleatorio import gerar_aleatorio
from lvl1.montar_tabuleiro import montar_tabuleiro
from lvl1.gerar_tabuleiro import gerar_tabuleiro
#level 2
from lvl2.transpor_matriz import transpor_matriz

#level 3
from lvl3.movimentar_tabuleiro import movimentar_tabuleiro
from lvl3.somar_tabuleiro import somar_tabuleiro
from lvl3.status_tabuleiro import status_tabuleiro

def main():
    #Exibindo menu com Banner do jogo gerado em figlet
    #Escrevendo regras na tela
    menu()
    #Gerando e montando o tabuleiro
    tabuleiro = gerar_tabuleiro(n=3)
    montar_tabuleiro(tabuleiro)
    status = True
    while status:
        #Recebendo, validando e recebendo como retorno a jogada
        #do usuário
        jogada = receber_jogada()
        tab_anterior = tabuleiro
        tabuleiro = movimentar_tabuleiro(tabuleiro,jogada)
        tabuleiro = somar_tabuleiro(tabuleiro,jogada)
        status = status_tabuleiro(tabuleiro)
        if status:
            tabuleiro = gerar_aleatorio(tabuleiro)
            montar_tabuleiro(tabuleiro)
    

main()