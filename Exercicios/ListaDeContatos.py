'''
3. Cadastro de Contatos com Dicionário
Nível: Intermediário
Objetivo: Praticar dicionários, listas e menus interativos.

Enunciado: Crie um sistema de cadastro de contatos que permita:

Adicionar um novo contato (nome, telefone, e-mail)

Buscar um contato pelo nome

Listar todos os contatos

Sair do programa

Use um loop para o menu e dicionários para armazenar os dados.'''

###################################################################

# Dicionário para armazenar os contatos, usando o nome como chave
contatos = {}

# Função para adicionar um novo contato
def adicionar_contato():
    # Coleta os dados do contato
    nome = input('Nome contato: ')
    telefone = input('Tefone: ')
    email = input('E-mail: ')
    
    # Armazena os dados no dicionário usando o nome como chave
    contatos[nome] = {"telefone": telefone, "email": email}
    
    # Confirmação de sucesso
    print(f"Contato {nome}, adicionado com sucesso✅")

# Função para listar todos os contatos salvos
def listar_contatos():
    print('\n 📖 Lista de Contatos')
    
    # Percorre cada item do dicionário
    for nome, info in contatos.items():
        # Mostra as informações de cada contato
        print(f'👨🏿‍💼 Nome: {nome}')
        print(f'☎ Telefone: {info["telefone"]}')
        print(f'✉ Email: {info["email"]}')
        print('-'*40)

# Função para buscar um contato pelo nome
def buscar_contato():
    nome = input('Digite o nome do contato que deseja busca: ')
    
    # Verifica se o nome está no dicionário
    if nome in contatos:
        print('Contato encontrado:')
        print(f'Telefone:  {contatos[nome]["telefone"]}')
        print(f'E-mail:  {contatos[nome]["email"]}')
    else:
        print('Contato não encontrado ❌')

# Loop principal do programa (menu interativo)
while True:
    print("\n=== Menu de Contatos ===")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Listar Contatos")
    print("4. Sair")
    
    # Lê a opção escolhida pelo usuário
    opcao = input("Escolha uma opção (1-4): ")

    # Verifica a opção e chama a função correspondente
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        listar_contatos()
    elif opcao == "4":
        print("Saindo... Até mais! 👋")
        break  # Encerra o loop e o programa
    else:
        print("Opção inválida! Tente novamente.")
