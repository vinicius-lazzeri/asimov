num1 = int(input('Insire um valor inteiro: '))
num2 = int(input('Insire outro valor inteiro: '))
num3 = int(input('Insire outro valor inteiro: '))

menor_numero = 0
maior_numero = 0

if num1 > num2 and num1 > num3:
    maior_numero = num1
elif num2 > num1 and num2 > num3:
    maior_numero = num2
elif num3 > num1 and num3 > num2:
    maior_numero = num3
if num1 < num2 and num1 < num3:
    menor_numero = num1
elif num2 < num1 and num2 < num3:
    menor_numero = num2
elif num3 < num1 and num3 < num2:
    menor_numero = num3
print(f'Menor numero: {menor_numero} | Maior numero: {maior_numero}')
