'''
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros numeros do CPF
multiplicando cada um dos valores por uma 
contagem regresiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3   2
  * 7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado por 10
301 * 10 = 3010
Obter o resto da divisao por 11
3010 % 11 = 7
Se o resultado for maior que 9:
    resultado é 0
caso contrario:
    resultado é o valor da conta

O primeiro digito do CPF é 7
'''

cpf = '746.824.890-72'

cpf_limpo = cpf.replace('.','').replace('-','')


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
print(digito_1)

dez_digitos_cpf = nove_digitos_cpf + str(digito_1)

for digito in dez_digitos_cpf:
    resultado_digito_2 += int(digito) * contador_regresivo_2
    contador_regresivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_verificado = dez_digitos_cpf + str(digito_2)

if cpf_verificado == cpf_limpo:
    print('CPF Válido')
else:
    print('CPF Inválido')
    


