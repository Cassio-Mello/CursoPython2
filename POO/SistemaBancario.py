'''
2. Sistema Bancário Simples
Crie uma classe ContaBancaria com nome do titular, saldo e número da conta.

Métodos:

depositar(valor)

sacar(valor)

exibir_saldo()

Crie dois objetos e simule transações.
'''

class ContaBancaria:
    def __init__(self, nome_titular, saldo, num_conta):
        self.nome_titular = nome_titular
        self.saldo = float(saldo)
        self.num_conta = num_conta

    def depositar(self, valor):
        self.saldo += float(valor)

    def sacar(self, valor):
        self.saldo -= float(valor)

    def exibir_saldo(self):
        print(f'{self.nome_titular} seu saldo é: {self.saldo:.2f} ')

c1 = ContaBancaria("Cássio", 1000, "12345-6")
c1.depositar(250)
c1.sacar(100)
c1.exibir_saldo()  # Deve mostrar: Cássio, seu saldo é: R$1150.00
