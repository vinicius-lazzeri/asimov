from math import ceil

m2_cliente = float(input('M² citado pelo cliente: '))

lata_de_tinta = 18
performance_tinta = lata_de_tinta * 3
preco_lata_tinta = 80

qtd_ideal_lata_tinta = m2_cliente / performance_tinta
qtd_ideal_lata_tinta = ceil(qtd_ideal_lata_tinta)

print(f'm² cliente = {m2_cliente} | qtd ideal = {(qtd_ideal_lata_tinta)} latas de tinta!')
print(f'Preço da lata de tinta = R${preco_lata_tinta:.2f} | Total = R${preco_lata_tinta*qtd_ideal_lata_tinta:.2f}')