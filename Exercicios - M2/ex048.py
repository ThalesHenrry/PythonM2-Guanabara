#Faça um programa que calcule a soma entre todos os numeros impares, que são multiplos de 3 e quee se encontram no intervalo de 1 até 500

for c in range(0, 500, 3):
    if c * 3 == 0:
        c = c
    c += c
print(f'A soma é {c}')

#996 ou 998