print('-=-' * 14)
operacao_calculadora = int(input((""""
C A L C U L A D O R A
=====================
Escolha uma operação!
[0] - Soma
[1] - Subtração
[2] - Multiplicação
[3] - Divisão
[4] - Exponenciação
Operação = """)))

while (operacao_calculadora != 5):
    if (operacao_calculadora >= 0 or operacao_calculadora <= 4):
        if operacao_calculadora == 0:
            print('=' * 14)
            print('OPERAÇÃO ESCOLHIDA → SOMA')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 + num2
            print(f'{num1} + {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 14)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            if nova_operacao == 1:
                operacao_calculadora = int(input((f""""
                    C A L C U L A D O R A
                    =====================
                    Escolha uma operação!
                    [0] - Soma
                    [1] - Subtração
                    [2] - Multiplicação
                    [3] - Divisão
                    [4] - Exponenciação
                    Operação = """)))
            elif nova_operacao == 2:
                operacao_calculadora = 5
            else:
                print('VALOR INVÁLIDO! POR FAVOR, DIGITE CONFORME ABAIXO!')
                operacao_calculadora = int(input((f""""
                                    C A L C U L A D O R A
                                    =====================
                                    Escolha uma operação!
                                    [0] - Soma
                                    [1] - Subtração
                                    [2] - Multiplicação
                                    [3] - Divisão
                                    [4] - Exponenciação
                                    Operação = """)))
        if operacao_calculadora == 1:
            print('=' * 14)
            print('OPERAÇÃO ESCOLHIDA → SUBTRAÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 - num2
            print(f'{num1} - {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 14)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            if nova_operacao == 1:
                operacao_calculadora = int(input((f""""
                    C A L C U L A D O R A
                    =====================
                    Escolha uma operação!
                    [0] - Soma
                    [1] - Subtração
                    [2] - Multiplicação
                    [3] - Divisão
                    [4] - Exponenciação
                    Operação = """)))
            elif nova_operacao == 2:
                operacao_calculadora = 5
            else:
                print('VALOR INVÁLIDO! POR FAVOR, DIGITE CONFORME ABAIXO!')
                operacao_calculadora = int(input((f""""
                                    C A L C U L A D O R A
                                    =====================
                                    Escolha uma operação!
                                    [0] - Soma
                                    [1] - Subtração
                                    [2] - Multiplicação
                                    [3] - Divisão
                                    [4] - Exponenciação
                                    Operação = """)))
        if operacao_calculadora == 2:
            print('=' * 14)
            print('OPERAÇÃO ESCOLHIDA → MULTIPLIÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 * num2
            print(f'{num1} * {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 14)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            if nova_operacao == 1:
                operacao_calculadora = int(input((f""""
                    C A L C U L A D O R A
                    =====================
                    Escolha uma operação!
                    [0] - Soma
                    [1] - Subtração
                    [2] - Multiplicação
                    [3] - Divisão
                    [4] - Exponenciação
                    Operação = """)))
            elif nova_operacao == 2:
                operacao_calculadora = 5
            else:
                print('VALOR INVÁLIDO! POR FAVOR, DIGITE CONFORME ABAIXO!')
                operacao_calculadora = int(input((f""""
                                    C A L C U L A D O R A
                                    =====================
                                    Escolha uma operação!
                                    [0] - Soma
                                    [1] - Subtração
                                    [2] - Multiplicação
                                    [3] - Divisão
                                    [4] - Exponenciação
                                    Operação = """)))
        if operacao_calculadora == 3:
            print('=' * 14)
            print('OPERAÇÃO ESCOLHIDA → DIVISÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 / num2
            print(f'{num1} ÷ {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 14)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            if nova_operacao == 1:
                operacao_calculadora = int(input((f""""
                    C A L C U L A D O R A
                    =====================
                    Escolha uma operação!
                    [0] - Soma
                    [1] - Subtração
                    [2] - Multiplicação
                    [3] - Divisão
                    [4] - Exponenciação
                    Operação = """)))
            elif nova_operacao == 2:
                operacao_calculadora = 5
            else:
                print('VALOR INVÁLIDO! POR FAVOR, DIGITE CONFORME ABAIXO!')
                operacao_calculadora = int(input((f""""
                                    C A L C U L A D O R A
                                    =====================
                                    Escolha uma operação!
                                    [0] - Soma
                                    [1] - Subtração
                                    [2] - Multiplicação
                                    [3] - Divisão
                                    [4] - Exponenciação
                                    Operação = """)))
        if operacao_calculadora == 4:
            print('=' * 14)
            print('OPERAÇÃO ESCOLHIDA → EXPONÊNCIAÇÃO!')
            num1 = float(input('Digite o 1° valor: '))
            num2 = float(input('Digite o 2° valor: '))
            soma = num1 ** num2
            print(f'{num1} ** {num2} = {soma}')
            print('OPERAÇÃO FINALIZADA!')
            print('=' * 14)
            nova_operacao = int(input('Deseja realizar uma nova operação? [1]SIM | [2]NÃO: '))
            if nova_operacao == 1:
                operacao_calculadora = int(input((f""""
                    C A L C U L A D O R A
                    =====================
                    Escolha uma operação!
                    [0] - Soma
                    [1] - Subtração
                    [2] - Multiplicação
                    [3] - Divisão
                    [4] - Exponenciação
                    Operação = """)))
            elif nova_operacao == 2:
                operacao_calculadora = 5
            else:
                print('VALOR INVÁLIDO! POR FAVOR, DIGITE CONFORME ABAIXO!')
                operacao_calculadora = int(input((f""""
                                    C A L C U L A D O R A
                                    =====================
                                    Escolha uma operação!
                                    [0] - Soma
                                    [1] - Subtração
                                    [2] - Multiplicação
                                    [3] - Divisão
                                    [4] - Exponenciação
                                    Operação = """)))
        if operacao_calculadora == 5:
            print('CALCULADORA FINALIZADA!')
print('[FIM DO PROGRAMA]')
