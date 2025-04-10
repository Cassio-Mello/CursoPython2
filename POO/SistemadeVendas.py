'''
6. Sistema de Vendas com Cliente e Pedido
Classe Cliente: nome, CPF.

Classe Produto: nome, preço.

Classe Pedido: cliente, lista de produtos.
    Método valor_total() para somar os preços.
'''

class Cliente:
    def __init__(self, nome, cpf):
        while True:
            try:   
                if not self.validar_cpf(cpf):
                    self.nome = nome
                    self.cpf = cpf
            
            except:
                print('❌CPF Inválido')
                
            



    def validar_cpf(self, cpf):
        cpf_limpo = cpf.replace('.','').replace('-','')

        if len(cpf_limpo) != 11 or not cpf_limpo.isdigit() or cpf_limpo == cpf_limpo[0] * 11:
            return False

        nove_digitos_cpf = cpf_limpo[0:9]


        contador_regresivo_1 = 10
        contador_regresivo_2 = 11

        resultado_digito_1 = 0
        resultado_digito_2 = 0

        for digito in nove_digitos_cpf:
            resultado_digito_1 += int(digito) * contador_regresivo_1
            contador_regresivo_1 -= 1



        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0


        dez_digitos_cpf = nove_digitos_cpf + str(digito_1)

        for digito in dez_digitos_cpf:
            resultado_digito_2 += int(digito) * contador_regresivo_2
            contador_regresivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
 

        cpf_verificado = dez_digitos_cpf + str(digito_2)

        if cpf_verificado == cpf_limpo:
            return True
        else:
            return False
        
class Produto:
    def __init__(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = float(preco)

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def somar_pedido(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        print(f'{total:.2f}')

    def somar_pedido2(self):
        total = sum(produto.preco for produto in self.produtos)
        print(f'{total:.2f}')
              
# Criando um cliente válido
cliente = Cliente("Cássio", "84499109000")

# Criando alguns produtos
produto1 = Produto("Café", 7.50)
produto2 = Produto("Pão", 2.00)
produto3 = Produto("Leite", 5.00)

# Criando um pedido para esse cliente
pedido = Pedido(cliente)

# Adicionando os produtos ao pedido
pedido.produtos.append(produto1)
pedido.produtos.append(produto2)
pedido.produtos.append(produto3)

# Mostrando o total do pedido
pedido.somar_pedido()
