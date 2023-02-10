# Desenvolva um programa que leia seis números inteiro  mostre a soma apenas daqueles que forem par. Impar desconsidere!

par = 0

for c in range(0, 6):
    num = int(input('Escreva um número: '))
    if num % 2 == 0:
        par = num + par
print(f'A soma dos números pares é {par}')
