# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
list_num = []
for c in range(0, 5):
    num = int(input('Um número: '))
    list_num.append(num)

for list_num in list_num:
    soma += list_num

print(f'A soma dos números é: {soma}\n'
      f'E a média é: {soma/5}')


