'''
Introdução as funçoes (def) em python
Funções sao trechos de codigo usados para
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
Por padaão funçoes python retornan None (nada).

'''
#def sem parametros
def imprimir():
    print('qualquer coisa')

#def com parametros
def imprimir_parametros(a, b, c):
    print(a, b, c)

imprimir()

imprimir_parametros(1, 2, 3)
imprimir_parametros(4, 5, 6)

def saudacao(nome):
    print(f'Olé, {nome}')

nome = input('informe seu nome:')

saudacao(nome)