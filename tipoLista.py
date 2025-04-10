'''
Listas em Pyrhon

tipo list - mutável
suporta valores de qualquer tipo
métodos uteis
    append, insert, pop, del, clear, extend, +
Create Read Update    Delete
Criar, ler, alterar,  apagar = lista[i] (CRUD)
'''

lista = [10, 20, 30, 40]

print(lista)
lista.append(50) #append adiciona valor ao final da lista
print(lista)

lista.pop() # pop() remove o ultimo valor da lista ou do [i] escolhido e retorna o valor removido
print(lista)

del lista[-1] #apaga um indice
print(lista)

# lista.clear() limpa a lista

lista.insert(2, 10)# insert(i, valor) adiciona um valor na lista no indice escolhido
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b #o sinal de + concatena(une) as duas listas
print(lista_c)

lista_a.extend(lista_b)# extende pega o valor da lista_b e adiciona a lista_a extendeu seu valor
print(lista_a)

