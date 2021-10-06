def receber_jogada():
    """ Lê uma jogada e confere se ela é válida """
    #Lista com as jogadas válidas
    validas = ["a","s","d","w"]
    while True:
        #Conferindo se a jogada faz parte do conjunto
        #de válidas
        jogada = str(input("Digite a jogada : "))
        if jogada.lower() in validas:
            return jogada.lower()
