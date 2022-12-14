nome = str(input('Digite seu nome: ')).strip().upper()
while len(nome) <= 3:
    print('O nome deve conter mais de 3 caracteres!')
    nome = str(input('Digite seu nome: ')).strip().upper()

idade = int(input('Idade: '))
while (idade <= 0 or idade >= 150):
    print('A idade deve estar entre 0 e 150!')
    idade = int(input('Idade: '))

salario = float(input('Salario: '))
while (salario <= 0):
    print('Salário deve ser maior que 0')
    salario = float(input('Salario: '))

sexo = str(input('Sexo [F/M]: ')).strip().upper()
while sexo not in ["F","M"]:
    print('O sexo deve ser "M" (Masc) ou "F"(Fem)!')
    sexo = str(input('Sexo [F/M]: ')).strip().upper()

estado_civil = str(input('Estado civil [S/C/V/D]: ')).strip().upper()
while estado_civil not in ["S", "C", "V", "D"]:
    print('Valor inválido! Digite S, C, V ou D! (SOLTEIRO/CASADO/VIÚVO/DIVORCIADO)')
    estado_civil = str(input('Estado civil [S/C/V/D]: ')).strip().upper()

print(f'NOME: {nome} | IDADE: {idade} ANOS | SEXO: {sexo}')
print(f'SALÁRIO: R${salario:.2f} |ESTADO CIVIL: {estado_civil}')
