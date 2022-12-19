
class Dog:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
        print(f'{raca} criado')

    def envelhecer(self):
        self.idade += 1
        return self.idade
dog = Dog("lab")
dog2 = Dog("husky")

print(dog.idade)
print(dog.raca)

print(dog2.idade)
print(dog2.raca)

#circulo

class Circle:
    def __init__(self, raio = 1):
        self.raio = raio

    def calcula_area(self):
        return self.raio * self.raio * 3.14

    def retorna_raio(self):
        return self.raio

c1 = Circle()
c2 = Circle(2)

c1.calcula_area()

c2.calcula_area()

c1.retorna_raio()

c2.retorna_raio()