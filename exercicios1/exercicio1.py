nome = str(input('Digite seu nome: ')).title()
peso = float(input('Digite seu peso em KGs: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'{nome} você tem {altura}m de altura, pesa {peso}KGs e tem IMC = {imc:.2f}')