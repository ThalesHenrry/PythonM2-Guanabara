#46
valor = 0

print('Especificação   Código  Preço\n'
      'Cachorro Quente 100     R$ 1,20\n'
      'Bauru Simples   101     R$ 1,30\n'
      'Bauru com ovo   102     R$ 1,50\n'
      'Hambúrguer      103     R$ 1,20\n'
      'Cheeseburguer   104     R$ 1,30\n'
      'Refrigerante    105     R$ 1,00')

cod = int(input('Código do pedido: '))
quant = int(input('Quantidade: '))

if cod == 100 or cod == 103:
    valor = quant * 1.20
elif cod == 101 or cod == 104:
    valor = quant * 1.30
elif cod == 102:
    valor = quant * 1.50
else:
    valor = quant * 1

print(f'Valor do item {valor}')
