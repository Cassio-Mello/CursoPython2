'''
4. Controle de Biblioteca
Classe Livro: título, autor, ano.

Classe Biblioteca: lista de livros.

Métodos da biblioteca:

adicionar_livro()

remover_livro(titulo)

listar_livros()
'''

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.ano})'


class Biblioteca:
    def __init__(self):
        self.livros = []  # Corrigido aqui

    def adicionar_livro(self, livro):  # Corrigido aqui
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            for livro in self.livros:
                print(livro)

    def remover_livro(self, titulo_remover):  # Corrigido aqui
        for livro in self.livros:
            if livro.titulo.lower() == titulo_remover.lower():
                self.livros.remove(livro)
                print('Livro removido.')
                return
        print('Livro não encontrado.')
