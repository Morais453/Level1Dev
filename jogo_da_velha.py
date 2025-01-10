global simbolo, jogador_da_vez,variavel_de_controle_jogo
def condicao_de_vitoria(tabuleiro,i):
    for l in range(0, 3):
    # VERIFICA LINHA
        if tabuleiro[l][0] == tabuleiro[l][1] == tabuleiro[l][2] != '':
            print(f'A vitória foi de {jogador_da_vez} na linha {l + 1}')
            variavel_de_controle_jogo = False  # INTERROMPE O LAÇO CONTINUO
            break  # INTERROMPE O 'FOR'

        # VERIFICA COLUNA
        elif tabuleiro[0][l] == tabuleiro[1][l] == tabuleiro[2][l] != '':
            print(f'A vitória foi de {jogador_da_vez} na coluna {l + 1}')

            variavel_de_controle_jogo = False
            break

        # VERIFICA AS DIAGONAIS
        elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or tabuleiro[0][2] == tabuleiro[1][1] == \
                tabuleiro[2][0]:
            print(f'A vitória foi de {jogador_da_vez}')
            variavel_de_controle_jogo = False
            break

        # SE CHEGAR A 9 JOGADAS SEM VITÓRIA DECLARAR EMPATE
        else:
            if i == 9:
                print('Empate')
                break

def jogo_da_velha():

    tabuleiro = [['','',''],['','',''],['','','']]

    while True:
        jogador_1 = input('Digite o nome do jogador 1: ')
        jogador_2 = input('Digite o nome do jogador 2: ')

        variavel_de_controle_de_jogador = [[jogador_1, 'X'],[jogador_2, 'O']]
        variavel_de_controle_jogo = True

        # JOGO EM SI, LAÇO CONT COM O N° MÁXIMO DE JOGADAS POSSIVEIS
        for i in range(9):
            # jogador_da_vez = variavel_de_controle_de_jogador[0][0], simbolo = variavel_de_controle_de_jogador[0][1] if i % 2 == 0 else jogador_da_vez = variavel_de_controle_de_jogador[1][0], simbolo = variavel_de_controle_de_jogador[1][1]
            if i % 2 == 0:  # DEFINIÇÃO DE NOME E SIMBOLO DE JOGADOR
                jogador_da_vez = variavel_de_controle_de_jogador[0][0]
                simbolo = variavel_de_controle_de_jogador[0][1]
            else:  # DEFINIÇÃO DE NOME E SIMBOLO DE JOGADOR
                jogador_da_vez = variavel_de_controle_de_jogador[1][0]
                simbolo = variavel_de_controle_de_jogador[1][1]

            print(f'É a vez do jogador {jogador_da_vez[0]}')

            # LAÇO CONTINUO
            while variavel_de_controle_jogo:

                # DEFINIÇÃO DA JOGADA, LINHA E COLUNA
                linha = int(input('Informe onde adicionar seu simbolo na linha[1,2,3]: ')) - 1
                coluna = int(input('Informe onde adicionar seu simbolo na coluna [1,2,3]: ')) - 1
                if tabuleiro[linha][coluna] == '':  # VERIFICAÇÃO SE A MATRIZ ESTÁ DISPONIVEL OU NÃO, SE SIM ADICIONA O SIMBOLO EQUIVALENTE AO JOGADOR E QUEBRA O LAÇO CONTINUO
                    tabuleiro[linha][coluna] = simbolo
                    break

                # SE NÃO ESCREVE QUE JÁ TEM ITEM E CONTINUA PEDINDO UMA COORDENADA PARA O SIMBOLO
                else:
                    print('Já contém item, tente novamente')

            print(f'''{tabuleiro[0][0]:^3}|{tabuleiro[0][1]:^3}|{tabuleiro[0][2]:^3}
            -----------\n{tabuleiro[1][0]:^3}|{tabuleiro[1][1]:^3}|{tabuleiro[1][2]:^3}
            -----------\n{tabuleiro[2][0]:^3}|{tabuleiro[2][1]:^3}|{tabuleiro[2][2]:^3}''')

            # VERIFICAR CONDIÇÃO DE VITÓRIA A PARTIR DA QUINTA JOGADA
            if i > 4:
                condicao_de_vitoria(tabuleiro,i)

            # SE A VARIAVEL DE CONTROLE RECEBER FALSE ANTES DO LOOP PRINCIPAL ACABAR, INTERROMPER O LOOP
            if variavel_de_controle_jogo == False:
                break

        escape = input('Voce quer continuar com uma nova partida?[S/N]').upper()
        while escape not in 'SN':
            escape = input('Voce quer continuar com uma nova partida?[S/N]').upper()
        if escape in 'S':
            tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
            continue
        else:
            break