# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

soma = 0
num = int(input('Digite um número: '))

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        soma += 1
    else:
        print('\033[32m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[m O número {num} foi divisivel {soma} vezes')
if soma == 2:
    print('E por isso é um número primo')
else:
    print('E por isso não é um número primo')