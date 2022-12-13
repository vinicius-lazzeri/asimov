from os import system

carros = [
        ("Chevrolet Tracker", 120),
        ("Chevrolet Onix", 90),
        ("Chevrolet Spin", 150),
        ("Hyundai HB20", 85),
        ("Hyundai Creta", 120),
        ("Fiat Mobi", 60),
        ("Fiat Argo", 70),
        ("Toyota Corolla", 130),
        ]

carros_alugados = []

def mostrar_portfolio_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - Custo: R${car[1]:.2f} por dia.')

while True:
    system('cls')

    print('=' * 35)
    print('« BEM-VINDO À LOCADORA DE CARROS! »')
    print('=' * 35)
    ordem_cliente = int(input('Qual serviço você deseja?\n[0] Mostrar carros disponíveis | [1] Alugar um carro | [2] Devolver um carro\nServiço escolhido: '))

    system('cls')
        
    if ordem_cliente == 0:
        print('=' * 48)
        mostrar_portfolio_carros(carros)

    elif ordem_cliente == 1:
        print('=' * 48)
        mostrar_portfolio_carros(carros)
        print('=' * 48)
        carro_solicitado = int(input('Digite o número do carro desejado: '))
        qtd_dias = int(input('Por quantos dias? '))
        system('cls')
        print('=' * 48)
        print(f'Carro escolhido: {carros[carro_solicitado][0]}\nQuantidade de dias: {qtd_dias} dias')
        print(f'Custo total: R${qtd_dias * carros[carro_solicitado][1]:.2f}')

        confirm = int(input('Confirmar aluguel?\n[0] SIM | [1] NÃO, DESEJO VER OUTRO MODELO!\n'))
        if confirm == 0:
            print(f'Parabéns! Carro alugado: {carros[carro_solicitado][0]}\nQuantidade de dias: {qtd_dias} dias!\nDirija com cuidado! ♥ ')
            carros_alugados.append(carros.pop(carro_solicitado))
    
    elif ordem_cliente == 2:
        if len(carros_alugados) == 0:
            print('Não há carros para devolver. ')
        else:
            print('Lista de carros alugados: ')
            mostrar_portfolio_carros(carros_alugados)
            print('Qual você deseja devolver?')
            carro_solicitado = int(input('Digite o número do carro a ser devolvido: '))
            if confirm == 0:
                print(f'Obrigado por devolver o carro {carros_alugados[carro_solicitado][0]}')
                carros.append(carros_alugados.pop(carro_solicitado))

    print('=' * 48)
    saida_cliente = int(input('Deseja sair do programa? [0] Não | [1] Sim \n'))
    
    if saida_cliente == 1:
        break