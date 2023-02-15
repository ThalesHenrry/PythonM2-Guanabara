from datetime import date

# Crie um progtama que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores

ano = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    nasc = int(input('Qual o seu ano de nascimento: '))
    idade = ano - nasc

    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print('')
print(f'Maior idade: {maior} pessoas;\n'
      f'Menor idade: {menor} pessoas.')
