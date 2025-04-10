#Exercicio - Sistema de Perguntas e Respostas

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5x5',
        'Opcoes': ['10', '25', '50', '75'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2',
        'Opcoes': ['4', '2', '5', '1'],
        'Resposta' : '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])
    print('-' * 40)

    opcoes = pergunta['Opcoes']
    for i,opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print('-' * 40)

    escolha = input('Escolha uma opção: ')

    escolha_Int = None
    acertou = False
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_Int = int(escolha)

    if escolha_Int is not None:
        if escolha_Int >= 0 and escolha_Int < qtd_opcoes:
            if opcoes[escolha_Int] == pergunta['Resposta']:
                acertou = True
    
    print('-' * 40)
    if acertou:
        qtd_acertos +=1
        print('Acertou ✔')
    else:
        print('Errou ❌')
    print('-' * 40)

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')