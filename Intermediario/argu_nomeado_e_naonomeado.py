'''
Argumento nomeado e nao nomeado
argumento nomeado tem nome com sinal de igual
argumento nao nomeado recebe apenas o argumento (valor)

'''

def soma(x, y, z):
    print(f'{x=} {y=} {x=} | x + y + z = ', x + y + z)

#argumento nao nomeado
soma(1, 2, 3)

#argumento nomeado
soma(x=4, y=5, z=6)
#argumento nomeado pode ser fora de ordem
soma(z=7, x=8, y=9)


#valor padrao
def multiplicar(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {x=} | x * y * z = ', x * y * z)
    else:
        print(f'{x=} {y=} | x * y = ', x * y)

multiplicar(1,2,3)
multiplicar(1,2)