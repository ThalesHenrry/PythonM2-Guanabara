# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# A vista din/cheque 10% desc | a vista catão 5% desc | 2x no cartão valor normal | 3x ou mais 20% de juros

valor_produto = float(input('Valor do produto R$'))
forma_pagamento = int(input(
    'Escolha sua forma de pagamento: \n'
    '[1] A vista Dinnheiro/Cheque\n'
    '[2] Cartão a vista \n'
    '[3] Cartão 2x \n'
    '[4] Cartão 3x ou + \n'
    'Escolha: '
))

if forma_pagamento == 1:
    valor_final = valor_produto - (valor_produto * 10 / 100)
elif forma_pagamento == 2:
    valor_final = valor_produto - (valor_produto * 5 / 100)
elif forma_pagamento == 3:
    valor_final = valor_produto
else:
    valor_final = valor_produto + (valor_produto * 20 / 100)

print(
    f' Com sua forma de pagamento, o valor do produto de R${valor_produto:.2f} para R${valor_final:.2f}'
)