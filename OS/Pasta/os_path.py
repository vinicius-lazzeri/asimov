import os

#Retorna uma string do caminho completo do diretório que o arquivo atual está.
os.getcwd()

#Retorna uma lista contendo todos os arquivos e pastas no diretório atual.
os.listdir()

#Retorna uma lista contendo todos os arquivos e pastas no diretório dado no método.
os.listdir('c:\\Users\\vinic\\')

#Troca o diretório padrão onde o código está sendo executado.
#os.chdir()
#O diretório estava em 'c:\\Users\\vinic\\OneDrive\\Documentos\\OS\\Pasta' e após a execução abaixo, ele foi para 'c:\\Users\\vinic\\'.
actual_dir = os.getcwd()
os.chdir('c:\\Users\\vinic\\')
print(os.getcwd())

#Cria uma pasta
os.mkdir('Pasta2')

#Renomeia uma pasta. Fórmula: 'os.rename('nome_atual.type', 'novo_nome.type')
os.rename('')

#Além de ter renomeado a pasta2 para pasta3, criou uma subpasta pasta2 dentro da pasta3.
os.rename('Pasta2', 'Pasta3/Pasta2')

#Remove arquivos do sistema operacional.
os.remove()

#Remove diretórios do sistema operacional. Utilizar com cuidado.
os.rmdir()

#Executa comandos do prompt de comando.
os.system('systeminfo')

#Mescla um caminho com outro(Melhor utilizado pois funciona independentemente do OS utilizado).
os.path.join(os.getcwd(), 'pasta')
#Também pode ser utilizado com a seguinte forma (mais ideal/prático):
os.getcwd() + '/pasta'

#Retorna a ultima pasta contida no caminho dentro do método.
os.path.basename(os.getcwd())

#Separa 'c:\\Users\\vinic\\OneDrive\\Documentos\\OS\\Pasta' em uma lista ['Users', 'OneDrive', 'Documentos', 'OS', 'Pasta'].
os.getcwd().split('\\')[-1]

#Quebra e transforma em uma tupla.
os.path.split(os.getcwd())

#Retorna tudo que vem antes da pasta dentro do método.
os.path.dirname(os.getcwd())

#Retorna o tempo.
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)

from datetime import datetime

datetime.utcfromtimestamp(lt)

#Boolean que retorna se o que está dentro do método é arquivo ou não (true or false)
os.path.isfile()

#Boolean que retorna se o que está dentro do método é diretório ou não (true or false)
os.path.isdir()