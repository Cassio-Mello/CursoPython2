import random

qtd_cpf = input("Informe quantos CPF's deseja gerar: ")

for _ in range(int(qtd_cpf)):
    nove_digitos_cpf = ''
    for j in range(9):
        nove_digitos_cpf += str(random.randint(0, 9))
    print(nove_digitos_cpf)