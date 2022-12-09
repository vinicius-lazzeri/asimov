from os import system
from time import sleep
operacao_calculadora = int(input(("""
C A L C U L A D O R A
=====================
Escolha uma operação!
[0] - Soma
[1] - Subtração
[2] - Multiplicação
[3] - Divisão
[4] - Exponenciação
=====================
Operação = """)))


while (operacao_calculadora != 5):
    if (operacao_calculadora >= 0 or operacao_calculadora <= 4):

        if operacao_calculadora == 0:
            print('=' * 21)
            print('↓ OPERAÇÃO ESCOLHIDA ↓\n         SOMA!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 + num2
            print(f'{num1} + {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 21)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            sleep(1.2)
            system('cls')
            if nova_operacao == 1:
                operacao_calculadora = 6
            elif nova_operacao == 2:
                operacao_calculadora = 5
                sleep(1.2)
                system('cls')
            else:
                print('VALOR INVÁLIDO! REINICIANDO A CALCULADORA!...')
                sleep(1.2)
                operacao_calculadora = 6

        if operacao_calculadora == 1:
            print('=' * 21)
            print('↓ OPERAÇÃO ESCOLHIDA ↓\n    SUBTRAÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 - num2
            print(f'{num1} - {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 21)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            sleep(1.2)
            system('cls')
            if nova_operacao == 1:
                operacao_calculadora = 6
            elif nova_operacao == 2:
                operacao_calculadora = 5
                sleep(1.2)
                system('cls')
            else:
                print('VALOR INVÁLIDO! REINICIANDO A CALCULADORA!...')
                sleep(1.2)
                operacao_calculadora = 6

        if operacao_calculadora == 2:
            print('=' * 21)
            print('↓ OPERAÇÃO ESCOLHIDA ↓\n    MULTIPLICAÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 * num2
            print(f'{num1} * {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 21)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            sleep(1.2)
            system('cls')
            if nova_operacao == 1:
                operacao_calculadora = 6
            elif nova_operacao == 2:
                operacao_calculadora = 5
                sleep(1.2)
                system('cls')
            else:
                print('VALOR INVÁLIDO! REINICIANDO A CALCULADORA!...')
                sleep(1.2)
                operacao_calculadora = 6

        if operacao_calculadora == 3:
            print('=' * 21)
            print('↓ OPERAÇÃO ESCOLHIDA ↓\n    DIVISÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 / num2
            print(f'{num1} ÷ {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 21)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            sleep(1.2)
            system('cls')
            if nova_operacao == 1:
                operacao_calculadora = 6
            elif nova_operacao == 2:
                operacao_calculadora = 5
                sleep(1.2)
                system('cls')
            else:
                print('VALOR INVÁLIDO! REINICIANDO A CALCULADORA!...')
                sleep(1.2)
                operacao_calculadora = 6

        if operacao_calculadora == 4:
            print('=' * 21)
            print('↓ OPERAÇÃO ESCOLHIDA ↓\n    EXPONÊNCIAÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 ** num2
            print(f'{num1} ** {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 21)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            sleep(1.2)
            system('cls')
            if nova_operacao == 1:
                operacao_calculadora = 6
            elif nova_operacao == 2:
                operacao_calculadora = 5
                sleep(1.2)
                system('cls')
            else:
                print('VALOR INVÁLIDO! REINICIANDO A CALCULADORA!...')
                sleep(1.2)
                operacao_calculadora = 6

        if operacao_calculadora == 6:
            operacao_calculadora = int(input((f"""
C A L C U L A D O R A
=====================
Escolha uma operação!
[0] - Soma
[1] - Subtração
[2] - Multiplicação
[3] - Divisão
[4] - Exponenciação
=====================
Operação = """)))

        if operacao_calculadora == 5:
            print('CALCULADORA FINALIZADA!')
            sleep(1.2)
            system('cls')

sleep(1.2)
print('Calculadora desenvolvida por Vinicius Lazzeri para o Curso da Asimov')
sleep(1.2)


