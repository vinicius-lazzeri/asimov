class Animal:
    def __init__(self):
        print('animal criado')
    
    def quem_ou_eu(self):
        print('eu sou um animal')

    def comer(self):
        print('comendo')

class Cachorro(Animal):
    def quem_ou_eu(self):
        print('eu sou um cachorro')
