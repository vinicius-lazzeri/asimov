from time import sleep
# Um número é PRIMO quando ele é divisível apenas por 1 e por ele mesmo.
n1 = int(input('Digite um número inteiro qualquer: '))
i = 0
print('Vamos verificar se o número que você escolheu é primo?')
sleep(1.5)
print('Analisando...')
sleep(2)
for c in range(1, n1+1):
    if n1 % c == 0:
        print('\033[34m', end=" ")
        i += 1
    else:
        print('\033[31m', end=" ")
    print(c, end=" ")
print(f'\033[m{n1} foi dividido {i} vez(es).')
if i > 2 or i == 1:
    print('\033[33m Ele não pode ser considerado PRIMO')
else:
    print('\033[32m Ele pode ser considerado PRIMO')