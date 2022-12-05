nome_funcionario = str(input('Digite o nome do colaborador: ')).title().strip()
valor_hora_funcionario = float(input('Insire seus ganhos por hora trabalhada: '))
hora_trabalho_funcionario = int(input('Quantas horas foram trabalhadas neste mês: '))

funcionario_salario_bruto = valor_hora_funcionario * hora_trabalho_funcionario
desconto_imposto_renda = funcionario_salario_bruto * 0.11
desconto_inss = funcionario_salario_bruto * 0.08
desconto_sindicato = funcionario_salario_bruto * 0.05
total_impostos = desconto_imposto_renda + desconto_inss + desconto_sindicato
funcionario_salario_liquido = funcionario_salario_bruto - total_impostos

print(f'COLABORADOR: {nome_funcionario} | SALÁRIO BRUTO = R${funcionario_salario_bruto:.2f}')
print(f'CUSTO I.R = R${desconto_imposto_renda:.2f} | CUSTO INSS = R${desconto_inss:.2f} | CUSTO SINDICADO = R${desconto_sindicato:.2f}')
print(f'DESCONTO TOTAL = R${total_impostos:.2f} | SALÁRIO LÍQUIDO = R${funcionario_salario_liquido:.2f}')