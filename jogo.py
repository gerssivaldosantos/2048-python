#Modulos feitos até agora e em ordem cronológica

#level 0
from lvl0.mover_zeros import mover_zeros
from lvl0.receber_jogada import receber_jogada
from lvl0.somar_adjacentes import somar_adjacentes
from lvl0.mensagem import mensagem
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
    #Exibindo Banner do jogo gerado em figlet
    #Escrevendo regras na tela
    mensagem()
    #Iniciando o record
    scores = []
    record = 0
    ficar_menu = True
    while ficar_menu:
        opcao = input(""" 
[ 0 ] Começar uma nova partida
[ 1 ] Exibir Record e Histórico de partidas
[ 2 ] Sair do jogo
Opção: """)
        if opcao == "0":
            menu_tamanho = True
            while menu_tamanho:
                tamanhos_validos = ["3","4","5","6","7","8","9"]
                tamanho = input("""
Escolha um tamanho de tabuleiro (3 - 9)
Tamanho :""")           
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
                tabuleiro = movimentar_tabuleiro(tabuleiro,jogada)
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
                print("""
-----------
|Tam |Score """)
            montar_tabuleiro(scores)
        elif opcao == "2":
            print("\nJogo Finalizado ! Até mais !\n")
            ficar_menu = False
        else:
            print("\nEntrada inválida, tente novamente ! \n")
                
main()