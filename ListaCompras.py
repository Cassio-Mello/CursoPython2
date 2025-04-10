import os

lista_compras = []

while True:
    print('        Informe a opçao desejada:          ')
    print('[i]nserir    [a]pagar    [l]istar    [s]air')

    opcao = input().lower()

    if opcao == 'i':
        os.system('cls')
        item = input('Adicione um ítem: ')
        lista_compras.append(item)
        

    elif opcao == 'a':
        item_excluir = input('Informe o numero do item que deseja excluir: ')

        try:
            indice = int(item_excluir)
            del lista_compras[indice]
            print('Ítem removido')

        except ValueError:
            print('Por favor digite um numero inteiro.')
        
        except IndexError:
            print('O indice informado não existe na lista.')

        except Exception:
            print('Erro descpnhecido.')

    elif opcao =='l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Lista vazia')

        for i, valor in enumerate(lista_compras):
            print(i, valor)

    elif opcao == 's':
        break
    else:
        print('OPÇÃO INVÁLIDA')

