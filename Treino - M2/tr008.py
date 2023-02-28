# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

qtd = int(input('Repetição: '))
lista = []
soma = 0

for c in range(0, qtd):
    num = int(input('Escreva um numero: '))
    if num < 0 or num > 100:
        print('Numero entre 0 e 100!')
    else:
        lista.append(num)

print(f'\nMaior numero {max(lista)}\n'
      f'Menos numero {min(lista)}\n')

for lista in lista:
    soma += lista
    
print(f'Soma dos valores digitados {soma}')
