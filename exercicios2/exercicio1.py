nome_aluno = str(input('Insire o nome do aluno(a): ')).strip().title()
nota1 = float(input(f'Nota AV1 do aluno(a) {nome_aluno}: '))
nota2 = float(input(f'Nota AV2 do aluno(a) {nome_aluno}: '))
media = (nota1 + nota2) / 2

if media == 10:
    print(f'ALUNO(A): {nome_aluno} | NOTA FINAL: {media:.2f} | SITUAÇÃO: APROVADO COM DISTINÇÃO!')
elif media >= 7:
    print(f'ALUNO(A): {nome_aluno} | NOTA FINAL: {media:.2f} | SITUAÇÃO: APROVADO!')
else:
    print(f'ALUNO(A): {nome_aluno} | NOTA FINAL: {media:.2f} | SITUAÇÃO: REPROVADO!')
print('FIM DO PROGRAMA')
