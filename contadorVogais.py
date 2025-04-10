#Crie um programa que solicite uma palavra ao usuário e conte quantas vogais (a, e, i, o, u) existem nela.

vogais = 'aeiou'
contador = 0

palavra = input('Digite uma palavra: ')

for letra in palavra.lower():
    if letra in vogais:
        contador += 1

print(contador)