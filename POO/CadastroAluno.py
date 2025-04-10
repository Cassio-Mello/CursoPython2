'''
1. Cadastro de Alunos
Crie uma classe Aluno com nome, matrícula e 3 notas.

Adicione um método media() que retorna a média das notas.

Adicione um método aprovado() que retorna se o aluno está aprovado (média ≥ 7).

Faça 3 objetos e mostre os resultados.

'''

class Aluno:
    def __init__(self, nome, matricula, nota1, nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        media = (float(self.nota1) + float(self.nota2) + float(self.nota3)) / 3
        return media
    
    def aprovado(self):
        if self.media() >= 7:
            print(f'Aluno: {self.nome}  -> APROVADO')
        else:
            print(f'Aluno: {self.nome}  -> REPROVADO')
