name = str(input('Insire um nome: ')).strip().upper()

for c in range (0, len(name), 1):
    print(name[:c+1])