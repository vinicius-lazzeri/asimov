from random import randint
from time import sleep

plays = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
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
    elif player == 2:
        print('PC VENCE!')
    else:
        print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
if pc == 1:  # PC joga PAPEL
    if player == 0:
        print('PC VENCE!')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
if pc == 2:  # PC joga TESOURA
    if player == 0:
        print('JOGADOR VENCE!')
    elif player == 1:
        print('PC VENCE!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida! Reinicie o programa e jogue adequadamente.')
sleep(2)
print('Fim de jogo')