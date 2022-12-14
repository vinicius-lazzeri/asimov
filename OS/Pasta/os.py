import os

#os.getcwd()

os.listdir("c:\\Users\\vinic")
actual_dir = os.getcwd()
os.chdir('c:\\Users\\vinic')
print(os.getcwd())
os.chdir(actual_dir)
print(os.getcwd())

os.mkdir('Pasta2')

os.rename('teste.txt', 'teste2.txt')
os.rename('Pasta3/Pasta2', 'Pasta2')

os.remove('Pasta')

os.rmdir('Pasta2')

os.system(cmd)
