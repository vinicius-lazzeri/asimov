from random import randint
from time import sleep

play_again = 0
placar_jogo = [0, 0]


while play_again != 1:
    plays = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print('-=-' * 14)
    print(f'Placar do jogo:\nJogador: {placar_jogo[0]}\nPC: {placar_jogo[1]}')
    print('-=-' * 14)
    print(""""Escolha seu movimento:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura""")
    player = int(input('E aí, qual será seu movimento? '))
    print('Será que você vai conseguir vencer?')
    sleep(1.5)
    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PÔ!')
    sleep(.5)
    print(f'Jogador jogou: {plays[player]} | PC jogou: {plays[pc]}')
    sleep(1.5)
    if pc == 0:  # PC joga PEDRA
        if player == 0:
            print('EMPATE!')
        elif player == 1:
            print('JOGADOR VENCE!')
            placar_jogo[0] += 1
        elif player == 2:
            print('PC VENCE!')
            placar_jogo[1] += 1
        else:
            print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
        play_again = int((input('Deseja jogar novamente? [0] SIM | [1] NÃO\n')))
        if play_again == 1:
            sleep(0.6)
            print('Finalizando o jogo...')
            sleep(0.6)
        else:
            sleep(0.6)
            print('Reiniciando...')
            sleep(0.6)
        
    if pc == 1:  # PC joga PAPEL
        if player == 0:
            print('PC VENCE!')
            placar_jogo[1] += 1
        elif player == 1:
            print('EMPATE!')
        elif player == 2:
            print('JOGADOR VENCE!')
            placar_jogo[0] += 1
        else:
            print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
        play_again = int((input('Deseja jogar novamente? [0] SIM | [1] NÃO\n')))
        if play_again == 1:
            sleep(0.6)
            print('Finalizando o jogo...')
            sleep(0.6)
        else:
            sleep(0.6)
            print('Reiniciando...')
            sleep(0.6)
    if pc == 2:  # PC joga TESOURA
        if player == 0:
            print('JOGADOR VENCE!')
            placar_jogo[0] += 1
        elif player == 1:
            print('PC VENCE!')
            placar_jogo[1] += 1
        elif player == 2:
            print('EMPATE!')
        else:
            print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
        play_again = int((input('Deseja jogar novamente? [0] SIM | [1] NÃO\n')))
        sleep(0.6)
        if play_again == 1:
            sleep(0.6)
            print('Finalizando o jogo...')
            sleep(0.6)
        else:
            sleep(0.6)
            print('Reiniciando...')
            sleep(0.6)
print('-=-' * 14)
print(f'Placar do jogo:\nJogador: {placar_jogo[0]}\nPC: {placar_jogo[1]}')
print('-=-' * 14)
sleep(2)
print('Fim de jogo')