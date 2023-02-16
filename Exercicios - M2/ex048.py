#Faça um programa que calcule a soma entre todos os numeros impares, que são multiplos de 3 e quee se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma é {soma}\n'
      f'Quantidade de números somados: {cont}')

#996 ou 998