from os import system

print('==' * 10)
operations = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "÷": "Divisão",
    "^": "Exponenciação",
}

while True:
    system("cls")
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("")
    op = int(input("Escolha a operação que deseja utilizar: "))
    op_string = list(operations.keys())[op]

    print("")
    print(f'Operação escolhida: {op_string}')
    print("")
    primeiro_valor = float(input("Qual primeiro valor? "))
    segundo_valor = float(input("Qual segundo valor? "))

    if op == 0:
        result = primeiro_valor + segundo_valor
    elif op == 1:
        result = primeiro_valor - segundo_valor
    elif op == 2:
        result = primeiro_valor * segundo_valor
    elif op == 3:
        result = primeiro_valor / segundo_valor
    elif op == 4:
        result = primeiro_valor ** segundo_valor
    print("")
    print(f'{primeiro_valor} {op_string} {segundo_valor} = {result}')
    print("")
    print('==' * 10)

    comando = int(input("Deseja realizar mais uma operação? [1] Sim | [2]Não "))
    if comando == 2:
        break
    