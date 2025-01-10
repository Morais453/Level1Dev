def condicao_de_vitoria(tabuleiro, jogador_da_vez):
    # Verifica linhas e colunas
    for l in range(3):
        if tabuleiro[l][0] == tabuleiro[l][1] == tabuleiro[l][2] != '':
            print(f'A vitória foi de {jogador_da_vez} na linha {l + 1}')
            return True
        if tabuleiro[0][l] == tabuleiro[1][l] == tabuleiro[2][l] != '':
            print(f'A vitória foi de {jogador_da_vez} na coluna {l + 1}')
            return True

    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '' or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        print(f'A vitória foi de {jogador_da_vez} na diagonal')
        return True

    return False

def imprimir_tabuleiro(tabuleiro):
    print(f'''
 {tabuleiro[0][0] or ' ':^3}|{tabuleiro[0][1] or ' ':^3}|{tabuleiro[0][2] or ' ':^3}
---+---+---
 {tabuleiro[1][0] or ' ':^3}|{tabuleiro[1][1] or ' ':^3}|{tabuleiro[1][2] or ' ':^3}
---+---+---
 {tabuleiro[2][0] or ' ':^3}|{tabuleiro[2][1] or ' ':^3}|{tabuleiro[2][2] or ' ':^3}
''')

def jogo_da_velha():
    while True:
        tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
        jogador_1 = input('Digite o nome do jogador 1: ')
        jogador_2 = input('Digite o nome do jogador 2: ')

        jogadores = [[jogador_1, 'X'], [jogador_2, 'O']]
        jogo_ativo = True

        for i in range(9):
            jogador_da_vez, simbolo = jogadores[i % 2]
            print(f'\nÉ a vez de {jogador_da_vez}')
            imprimir_tabuleiro(tabuleiro)

            # Jogada do jogador
            while True:
                try:
                    linha = int(input('Informe a linha [1-3]: ')) - 1
                    coluna = int(input('Informe a coluna [1-3]: ')) - 1
                    if 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == '':
                        tabuleiro[linha][coluna] = simbolo
                        break
                    else:
                        print('Posição inválida ou já ocupada. Tente novamente.')
                except ValueError:
                    print('Entrada inválida. Use números entre 1 e 3.')

            # Verifica condição de vitória
            if i >= 4 and condicao_de_vitoria(tabuleiro, jogador_da_vez):
                imprimir_tabuleiro(tabuleiro)
                jogo_ativo = False
                break

        if jogo_ativo:  # Se nenhum jogador venceu após 9 rodadas
            print('Empate!')
            imprimir_tabuleiro(tabuleiro)

        # Pergunta se os jogadores querem jogar novamente
        continuar = input('Deseja jogar novamente? [S/N]: ').strip().upper()
        while continuar not in ['S', 'N']:
            continuar = input('Resposta inválida. Deseja jogar novamente? [S/N]: ').strip().upper()
        if continuar == 'N':
            break

jogo_da_velha()