print('Escolha o tipo de tabuada:\n'
      '[1] Multiplicação\n'
      '[2] Adição\n'
      '[3] Subtração\n'
      '[4] Divisão')
escolha = int(input('Escolha:'))

num = int(input('Escolha um número: '))

if escolha == 1:
    for c in range(1, 11):
        print(f'{num} X {c:2} = {num * c} ')
    print('')
elif escolha == 2:
    for c in range(1, 11):
        print(f'{num} + {c:2} = {num + c}')
    print('')
elif escolha == 3:
    for c in range(1, 11):
        print(f'{num} - {c:2} = {num - c}')
    print('')
elif escolha == 4:
    for c in range(1, 11):
        print(f'{num} / {c:2} = {abs(num / c):.2f}')
    print('')
else:
    print('Valor incorreto!')
