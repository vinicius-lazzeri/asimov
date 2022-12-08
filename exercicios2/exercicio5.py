nome = str(input('insire um nome: ')).strip().upper()
idade = int(input('idade: '))
salario = float(input('salario: '))
sexo = str(input('sexo [F/M]: ')).strip().upper()
estado_civil = str(input('estado civil [S/C/V/D]: ')).strip().upper()
#condição nome
if len(nome) > 3:
    nome = (f'NOME: {nome}')
else:
    print('valor inválido! insira seu nome completo!')
    nome = str(input('insire um nome: '))
#condição idade
    if idade < 0 and idade > 150:
        print('valor inválido! digite uma idade entre 0 e 150.')
        idade = int(input('idade: '))
    else:
        idade = (f'IDADE: {idade} anos')
#condição salário
    if salario > 0:
        salario = (f'SALARIO = R${salario:.2f}')
    else:
        print('valor inválido! insira seu salário novamente!')
        salario = float(input('salario: '))
        salario = (f'SALARIO = R${salario:.2f}')
    #condição sexo
if sexo == 'F' or sexo == 'M':
    if sexo == 'F':
        sexo = ('SEXO: FEMININO')
    else:
        sexo = ('SEXO: MASCULINO')
else:
    print('valor inválido! insira F para feminino e M para masculino!')
    sexo = str(input('sexo [F/M]: '))
    if sexo == 'F' or sexo == 'M':
        if sexo == 'F':
            sexo = ('SEXO: FEMININO')
        else:
            sexo = ('SEXO: MASCULINO')

#condição estado civil
if estado_civil == 'S' or estado_civil == 'C' or estado_civil == 'V' or estado_civil == 'D':
    if estado_civil == 'C':
        estado_civil = (f'ESTADO CIVIL: CASADO(A)')
    elif estado_civil == 'S':
        estado_civil = (f'ESTADO CIVIL: SOLTEIRO(A)')
    elif estado_civil == 'V':
        estado_civil = (f'ESTADO CIVIL: VIÚVO(A)')
    elif estado_civil == 'D':
        estado_civil = (f'ESTADO CIVIL: DIVORCIADO(A)')
else:
    print('VALOR INVÁLIDO! DIGITE [S/C/V/D] (SOLTEIRO/CASADO/VIÚVO/DIVORCIADO')
    estado_civil = str(input('estado civil [S/C/V/D]: '))
    if estado_civil == 'C':
        estado_civil = (f'ESTADO CIVIL: CASADO(A)')
    elif estado_civil == 'S':
        estado_civil = (f'ESTADO CIVIL: SOLTEIRO(A)')
    elif estado_civil == 'V':
        estado_civil = (f'ESTADO CIVIL: VIÚVO(A)')
    elif estado_civil == 'D':
        estado_civil = (f'ESTADO CIVIL: DIVORCIADO(A)')

print(f'INFORMAÇÕES: {nome} | {idade} | {sexo}')
print(f'{salario} | {estado_civil}')