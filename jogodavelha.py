from time import sleep
from random import randint

layout = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

jogador = 'X'
num_jogadas = 0

for lin in layout:
    for col in lin:
        print(f'|{col}', end='')
    print('|')

while True:
    #Resultado da linha e da coluna 1:
    if layout[0][0] + layout[0][1] + layout[0][2] == 'XXX' or layout[0][0] + layout[1][0] + layout[2][0] == 'XXX':
        print('Boa! Você venceu!')
        break
    elif layout[0][0] + layout[0][1] + layout[0][2] == 'OOO' or layout[0][0] + layout[1][0] + layout[2][0] == 'OOO':
        print('PC levou essa!')
        break
    #Resultado da linha e da coluna 2:
    if layout[1][0] + layout[1][1] + layout[1][2] == 'XXX' or layout[0][1] + layout[1][1] + layout[2][1] == 'XXX':
        print('Boa! Você venceu!')
        break
    elif layout[1][0] + layout[0][1] + layout[1][2] == 'OOO' or layout[0][1] + layout[1][0] + layout[2][1] == 'OOO':
        print('PC levou essa!')
        break
    #Resultado da linha e da coluna 3:
    if layout[2][0] + layout[2][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][2] + layout[2][2] == 'XXX':
        print('Boa! Você venceu!')
        break
    elif layout[2][0] + layout[2][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][2] + layout[2][2] == 'OOO':
        print('PC levou essa!')
        break
    #Resultado vertical:
    if layout[0][0] + layout[1][1] + layout[2][2] == 'XXX' or layout[0][2] + layout[1][1] + layout[2][0] == 'XXX':
        print('Boa! Você venceu!')
        break
    elif layout[0][0] + layout[1][1] + layout[2][2] == 'OOO' or layout[0][2] + layout[1][1] + layout[2][0] == 'OOO':
        print('PC levou essa!')
        break
    #Resultado caso empate:
    elif num_jogadas == 9:
        print('Velhou!')
        break

    if jogador == 'X':
        print('Faça sua jogada!')
        while True:
            try:
                l = int(input('Linha: '))
                c = int(input('Coluna: '))
                if ' ' in layout[l][c]:
                    layout[l][c] =  jogador
                    jogador = 'O'
                    break
                else: 
                    print('Este campo já foi preenchido')
            except:
                print('Jogada inválida')
        sleep(0.8)
    
    elif jogador == '0':
        print('Vez do PC')
        while True:
            l = randint(0, 2)
            c = randint(0, 2)
            if ' ' in layout [l][c]:
                layout [l][c] = jogador
                jogador = 'X'
                break
        sleep(0.8)

    num_jogadas += 1

    for lin in layout:
        for col in lin:
            print(f'|{col}', end='')
        print('|')

