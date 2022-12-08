from time import sleep
num_fibonacci = int(input('Qual tamanho da sequência de fibonacci você deseja ver? '))
v0 = 0
v1 = 1
v = 1
print("Começando! 1...")
sleep(1.2)
for i in range(num_fibonacci+1):
    print(v, end=" ")
    v0 = v1
    v1 = v
    v = v1 + v0