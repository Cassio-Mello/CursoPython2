import random

numero_oculto = random.randint(1, 100)
numero_digitado = 0
tentativas = 0

while True:
    tentativas +=1
    try:
        numero_digitado = int(input('Tente adivinhar o número ocoulto! Digite um numero:'))

        if numero_digitado == numero_oculto:
            print(f'Parabens! Você Acertou em {tentativas} tentativas!!!')
            break
        elif numero_digitado > numero_oculto:
            print('O numero é menor que o informado')
        else:
            print('O numero é maior que o informado')
    except ValueError:
        print('Digite um numero Válido')