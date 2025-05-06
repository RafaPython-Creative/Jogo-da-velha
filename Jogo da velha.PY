tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

jogador = 'X'
# esse def exibe o tabuleiro na tela, e organiza o tabuleiro em linhas e colunas
def exibeTabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

 # Verifica se a posição informada é válida:
 # - linha e coluna devem estar entre 0 e 2
 # - e a célula precisa estar vazia (' ')
def jogada(linha, coluna):
    if (
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != ' '
    ):
        print('Jogada inválida!')
        return jogador # Se for inválida, mantém o mesmo jogador
    tabuleiro[linha][coluna] = jogador # Se for válida, registra a jogada no tabuleiro
    return 'O' if jogador == 'X' else 'X'  # Alterna o jogador para a próxima rodada

def temGanhador():
    """ Verifica as linhas """
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and 
            tabuleiro[linha][0] == tabuleiro[linha][2]
        ):
            print(f'{tabuleiro[linha][0]} GANHOU!!!')
            return True

    """ Verifica as colunas """
    for coluna in range(3):
        if (
            tabuleiro[0][coluna]!= ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and 
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f'{tabuleiro[0][coluna]} GANHOU!!!')
            return True
    
    """ Verifica as diagonais """
    if (
        tabuleiro[1][1] != ' ' and
        (
            (
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            ) or
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )
    ):
            print(f'{tabuleiro[1][1]} GANHOU!!!')
            return True

    """ Se não teve ganhador em nenhuma forma """
    return False

#esse codigo verifica se houve empate, ou seja, se o tabuleiro está cheio e não houve ganhador
#se o tabuleiro estiver cheio e não houver ganhador, o jogo acaba empatado
def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print('Acabou empatado!')
    return True

# esse codigo é um loop infinito, o jogo só acaba quando o jogador ganhar ou empatar
# ele tem condições para verificar se o jogador digitou valores válidos, se o jogador já jogou naquela posição e se o jogo acabou
# o jogador só pode jogar se a posição estiver vazia, se não estiver ele vai ter que jogar novamente
while True:
    print(f'Jogador da vez: {jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores numéricos entre 0 e 2!')
    except ValueError:
        print('Os valores devem ser números inteiros!')
    exibeTabuleiro()

#finaliza o jogo se houver ganhador ou empate
    if temGanhador() or temEmpate():
        print('Fim de jogo!')
        break