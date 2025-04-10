#Crie um programa que solicite uma palavra ao usuário e conte quantas vogais (a, e, i, o, u) existem nela.

def contar_vogais(palavra):
    vogais = 'aeiou'
    contador = 0
    for letra in palavra.lower():
        if letra in vogais:
            contador += 1
    return contador

palavra = input('Digite uma palavra: ')

qtd_vogais = contar_vogais(palavra)

print(qtd_vogais)
