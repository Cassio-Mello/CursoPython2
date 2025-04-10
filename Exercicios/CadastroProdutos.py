'''
🧾 2. Sistema de Cadastro de Produtos com Busca
Crie um programa que:

Permite adicionar produtos (nome, preço e categoria).

Salva tudo em um dicionário ou lista.

Permite buscar produtos por nome ou categoria.

Mostra a lista completa ordenada por preço (use sorted()).

Desafio extra: salvar os dados em um arquivo .json.
'''

###############################################################

products = {}

# Dicionário para armazenar os produtos
products = {}

# Função para registrar um produto
def register_product():
    name_product = input('Insert the product name: ').strip().title()  # Remove espaços e padroniza
    if name_product in products:
        print('⚠️ Product already registered!')
        return
    
    try:
        price_product = float(input('Price: '))  # Converte para número
    except ValueError:
        print('❌ Invalid price. Use numbers like 10.50')
        return

    category = input('Category: ').strip().title()

    # Salva no dicionário com nome como chave
    products[name_product] = {'price': price_product, 'category': category}
    
    print('✅ Product successfully saved!')

def search_by_name():
    name = input('Enter the product name: ').strip().title()

    if name in products:
        print(f'🔎 Found: {name}')
        print(f'💰 Price: R${products[name]['price']}:.2f')
        print(f'📦 Category: {products[name]['category']}')
    else:
        print(f'❌ Product {name} not found')

def search_by_category():
    category_search = input('Enter the category: ').strip().tilte()
    found = False

    print(f'Products in category {category_search}')
    for name, data in products.items():
        if data['category'] == category_search:
            print(f'🛒{name} - R$ {data['price']:.2f}')
            found = True

    if not found:
            print('⚠ No products found in this category.')

def list_by_price():
    print('n\ List of products (ordered by price)')

    # sorted() vai ordenar com base em: produto[1]["price"]
    ordered_products = sorted(products.items(), key=lambda item: float(item[1['price']]))

    for name, data in ordered_products:
        print(f'🛒 {name} - R$ {float(data['price']):.2f} | Categoria: {data['category']}')



