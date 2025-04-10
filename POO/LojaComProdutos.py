'''
3. Loja com Produtos
Classe Produto com nome, preço e quantidade em estoque.

Método vender(qtd) que reduz o estoque se houver quantidade.

Método repor(qtd) para adicionar estoque.

Crie 2 produtos e simule vendas e reposições.

'''

class Produto:
    def __init__(self, nome_produto, preco, estoque):
        self.nome_produto = nome_produto
        self.preco = float(preco)
        self.estoque = int(estoque)

    def vender(self, qtd_venda):
        qtd_venda_int = int(qtd_venda)
        if self.estoque > 0 and self.estoque >= qtd_venda_int:
            self.estoque -= qtd_venda_int
            print('Venda realizada com sucesso')
        else:
            print('Estoque insuficiente')

    def repor(self, qtd_repor):
        qtd_repor_int = int(qtd_repor)
        self.estoque += qtd_repor_int

