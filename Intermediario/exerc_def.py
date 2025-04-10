#crie uma função que multiplique todos os argumentos não nomeados recebidos
#retorna o total para uma variavel e mostra o valor

def multiplicar(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

calculo = multiplicar(1, 2, 3, 4, 5, 6)
print(calculo)

#crie uma função que fala se o numero é oar ou umpar

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(1))
print(par_impar(2))
print(par_impar(3))
print(par_impar(4))
print(par_impar(15))
print(par_impar(6))
