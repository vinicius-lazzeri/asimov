name = str(input('Insire um nome: ')).strip().upper()

for c in range (0, len(name), 1):
    nome = name[:c+1]
    print(nome)