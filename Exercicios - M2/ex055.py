# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lido

maior = 0
menor = float("inf")

for c in range(0, 5):
    peso = float(input('Qual o seu peso: '))
    if maior < peso:
        maior = peso

    if menor > peso:
        menor = peso

print('')
print(f'Maior peso: {maior}Kg;\n'
      f'Menor peso: {menor}Kg.')
