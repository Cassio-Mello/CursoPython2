class Personagem:
    def __init__(self, nome, nivel, vida):
        self.nome = nome
        self.nivel = nivel
        self.vida = vida

    def apresentar(self):
        print(f'Nome: {self.nome}, Nivel: {self.nivel}, Vida: {self.vida}')

    def atacar(self):
        print('soco')

class Guerreiro(Personagem):
    def atacar(self):
        print(f'{self.nome} ataca com a espada')

class Mago(Personagem):
    def atacar(self):
        print(f'{self.nome} ataca com bola de fogo')

class Arqueiro(Personagem):
    def atacar(self):
        print(f'{self.nome} dispara uma flecha')

g1 = Guerreiro("Thorin", 10, 120)
m1 = Mago("Gandalf", 20, 80)
a1 = Arqueiro("Legolas", 15, 100)

g1.apresentar()
g1.atacar()

m1.apresentar()
m1.atacar()

a1.apresentar()
a1.atacar()
