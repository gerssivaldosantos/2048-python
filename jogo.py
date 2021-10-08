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
from lvl2.status_tabuleiro import status_tabuleiro
#level 3
from lvl3.movimentar_tabuleiro import movimentar_tabuleiro

def main():
    #Exibindo menu com Banner do jogo gerado em figlet
    #Escrevendo regras na tela
    menu()
    #Gerando e montando o tabuleiro
    tabuleiro = gerar_tabuleiro(n=4)
    montar_tabuleiro(tabuleiro)
    while True:
    
        #Recebendo, validando e recebendo como retorno a jogada
        #do usuário
        jogada = receber_jogada()
        tabuleiro = movimentar_tabuleiro(tabuleiro,jogada)
        montar_tabuleiro(tabuleiro)
    

main()