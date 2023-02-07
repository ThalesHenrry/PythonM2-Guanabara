#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 par bínario | 2 para octal| 3 para hexadecimal

num = int(input('Digite um número: '))
escolha = int(input(
    'Escolha a opção que deseja para a conversão do número:\n'
    '[1] Bínário\n'
    '[2] Octadecimal\n'
    '[3] Hexadecimal\n'
    'Escolha: '
))

if escolha == 1:
    conv = bin(num)
    print(f'O número escolhido foi {num}\n'
          f'Em Bínario: {conv[2::]}')
elif escolha == 2:
    conv = oct(num)
    print(f'O número escolhido foi {num}\n'
          f'Em Octademical: {conv[2::]}')
else:
    conv = hex(num)
    print(f'O número escolhido foi {num}\n'
          f'Em Hexadecimal: {conv[2::]}')