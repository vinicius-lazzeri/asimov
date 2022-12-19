from random import choice
from os import system

move_list = ['papel', 'pedra', 'tesoura']
placar_jogo = [0, 0]

print('=' * 35)
print('Bem vindo ao jogo: Pedra, papel e tesoura!')
print('=' * 35)

def main_print():
    print('=' * 35)
    print(f'PLACAR DO JOGO | PLAYER 1 VS PC\nPLAYER 1: {placar_jogo[0]}\nPC: {placar_jogo[1]}\n')
    print(input('Escolha seu lance!\n[0] Pedra | [1] Papel | [2] Tesoura\n'))

def select_move():
    return choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        
        except Exception as e:
            print(e)

def select_winner(p_move, c_move):
    global placar_jogo

    if p_move == 'papel':
        if c_move == 'pedra':
            placar_jogo[0] += 1
            return 'p'
        elif c_move == 'tesoura':
            placar_jogo[1] += 1
            return 'c'
        else:
            return 'd'
    
    if p_move == 'pedra':
        if c_move == 'papel':
            placar_jogo[1] += 1
            return 'c'
        elif c_move == 'tesoura':
            placar_jogo[0] += 1
            return 'p'
        else:
            return 'd'
    
    if p_move == 'tesoura':
        if c_move == 'papel':
            placar_jogo[0] += 1
            return 'p'
        elif c_move == 'pedra':
            placar_jogo[1] += 1
            return 'c'
        else:
            return 'd'

again = 1

while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)
    print('=' * 35)
    print(f'Sua jogada: {player_move}\nJogada do PC: {computer_move}')

    if winner == 'p':
        print('Player 1 venceu!')
    elif winner == 'c':
        print('PC vence!')
    else:
        print('Empate!')
    print('=' * 35)

    while True:
        next = int(input('Jogar novamente?\n[0] SIM | [1] NÃO\n'))
        if next == 0:
            break
        elif next == 1:
            again = 0
            print(f'PLACAR DO JOGO | PLAYER 1 VS PC\nPLAYER 1: {placar_jogo[0]}\nPC: {placar_jogo[1]}\n')
            break
    system('cls')
