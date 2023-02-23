# Faça um programa que leia 5 números e informe o maior número.

maior = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    maior.append(num)

print(f'O \033[1;31mmaior\033[m número é {max(maior)}')
print(f'O \033[1;32mmenor\033[m número é {min(maior)}')
