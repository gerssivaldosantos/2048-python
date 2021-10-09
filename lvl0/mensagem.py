""" Crie um menu para o jogo, que informa como o jogo ´e jogado, quais s˜ao as teclas
v´alidas. N˜ao precisa estar perfeito, pois ao juntar tudo no programa principal,
talvez precisem mudar. """


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
    


