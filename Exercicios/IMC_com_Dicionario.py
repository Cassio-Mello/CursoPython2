'''🧮 Exercício 1 – Calculadora de IMC com Dicionário
Enunciado:
Crie um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa e
 armazene as informações em um dicionário.
O programa deve:

Solicitar o nome, peso (em kg) e altura (em metros) do usuário.

Calcular o IMC usando a fórmula: IMC = peso / (altura ** 2).

Armazenar o nome, peso, altura e o IMC calculado no dicionário.

Exibir a situação do usuário com base no IMC:

Abaixo de 18.5: Abaixo do peso

Entre 18.5 e 24.9: Peso ideal

Entre 25 e 29.9: Sobrepeso

30 ou mais: Obesidade
'''
 #1 armazene as informações em um dicionário.

peaple = {}

#2 Solicitar o nome, peso (em kg) e altura (em metros) do usuário.

name = input('Enter name: ')
weigth = float(input('Enter weigth: '))
heigth = float(input('Enter heigth: '))

#3 Calcular o IMC usando a fórmula: IMC = peso / (altura ** 2).
imc = weigth / (heigth ** 2)

#4 Armazenar o nome, peso, altura e o IMC calculado no dicionário.
peaple['name'] = name
peaple['weigth'] = weigth
peaple['heigth'] = heigth
peaple['imc'] = round(imc, 2)


# Exibir a situação do usuário com base no IMC:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso ideal
# Entre 25 e 29.9: Sobrepeso
# 30 ou mais: Obesidade

print(f'\n {peaple['name']}, your IMC is: {peaple['imc']}')

if imc < 18.5:
    print('Situation: underweigth')
elif imc < 25:
    print('Situação: ideal wegigth')
elif imc < 30:
    print('Situation: overweigth')
else:
    print('Situation: obesity')

