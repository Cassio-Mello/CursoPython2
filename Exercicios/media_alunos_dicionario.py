'''
📚 Exercício 2 – Cadastro de Alunos e Médias com Dicionário
Enunciado:
Faça um programa que cadastre alunos e suas notas utilizando um dicionário.
O programa deve:

Permitir o cadastro do nome de 3 alunos.

Para cada aluno, solicitar 3 notas (valores de 0 a 10).

Armazenar as notas em uma lista associada ao nome do aluno no dicionário.

Ao final, exibir um boletim com o nome de cada aluno, suas notas e a média final.
'''

# Dicionário para armazenar os alunos e suas respectivas notas
student = {}

# Loop para cadastrar 3 alunos
for _ in range(3):
    name = input('Enter student name: ')  # Solicita o nome do aluno
    grades = []  # Lista para armazenar as 3 notas do aluno

    # Loop para coletar 3 notas por aluno
    for i in range(1, 4):
        while True:
            try:    
                # Tenta converter a entrada para float
                grade = float(input(f'Grade {i}: '))
                grades.append(grade)  # Adiciona a nota na lista
                break  # Sai do loop se a nota for válida
            except ValueError:
                # Mostra mensagem de erro caso a entrada não seja um número válido
                print('❌Invalid Value! Enter a value like 7 or 8.5')

    # Associa o nome do aluno à sua lista de notas no dicionário
    student[name] = grades

# Função que exibe o boletim dos alunos
def grade_list():
    print('Bulletin Students')

    # Percorre o dicionário de alunos
    for name, grades in student.items():
        print(f'Student: {name}')

        # Mostra cada nota usando enumerate para numerar
        for i, grade in enumerate(grades, start=1):
            print(f'    nota {i}: {grade}')

        # Calcula e exibe a média das notas do aluno, com 2 casas decimais
        average = sum(grades) / len(grades)
        print(f'        Average:{round(average, 2)}')

# Chama a função para mostrar o boletim de todos os alunos
grade_list()

