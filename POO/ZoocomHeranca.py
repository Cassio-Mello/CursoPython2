'''
5. Zoológico com Herança
Classe base Animal: nome, idade.

Subclasses:

Leao: rugido específico.

Macaco: som de macaco.

Elefante: trombeta.

Todos herdam um método falar() que é sobrescrito.
'''

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print('Som do animal')

class Leao(Animal):
    def falar(self):
        print('rugido de leão')

class Macaco(Animal):
    def falar(self):
        print('som de macaco')

class Elefante(Animal):
    def falar(self):
        print('trombeta')