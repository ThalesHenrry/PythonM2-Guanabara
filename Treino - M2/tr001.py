from time import sleep
# 46
valor = 0
total = 0
cont = 0
while cont == 0:
    print('\033[1;47;30mEspecificação\033[m   \033[1;47;30mCódigo\033[m  \033[1;47;30mPreço\033[m\n'
          'Cachorro Quente 100     R$ 1,20\n'
          'Bauru Simples   101     R$ 1,30\n'
          'Bauru com ovo   102     R$ 1,50\n'
          'Hambúrguer      103     R$ 1,20\n'
          'Cheeseburguer   104     R$ 1,30\n'
          'Refrigerante    105     R$ 1,00')
    print(' ')
    cod = int(input('Código do pedido: '))
    quant = int(input('Quantidade: '))

    if cod == 100 or cod == 103:
        valor = quant * 1.20
    elif cod == 101 or cod == 104:
        valor = quant * 1.30
    elif cod == 102:
        valor = quant * 1.50
    elif cod == 105:
        valor = quant * 1
    else:
        print('\033[1;31mCódigo Inválido!\033[m')
    print(' ')
    print('_'*10)
    print(f'Pedido:{cod}\n'
          f'Quantidade: {quant}\n'
          f'R${valor:.2f}')
    print('_' * 10)
    total += valor
    print(' ')
    esc = int(input('\033[1m[1]\033[m \033[1;32mFazer mais um pedido?\033[m\n'
                    '\033[1m[2]\033[m \033[1;31mEncerrar.\033[m\n'
                    '\033[1mEscolha: \033[m'))

    print(' ')

    if esc == 2:
        cont = 2

print('\033[1mCalculando valor', end='')
sleep(0.5)
print('\033[1m.', end='')
sleep(0.5)
print('\033[1m.', end='')
sleep(0.5)
print('\033[1m.')

print('\033[1;33m=-=PEDIDO FINALIZADO=-=\033[m')
print(f'\033[1mTOTAL A PAGAR\033[m \033[1;32mR${total:.2f}\033[m')