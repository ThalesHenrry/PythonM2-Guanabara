from datetime import date

# Crie um progtama que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores

ano = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f'Participante número {c}º, qual o seu ano de nascimento: '))
    idade = ano - nasc

    if idade >= 18:
        maior += 1
    else:
        menor += + 1

print('')
print(f'Maior idade: \033[1m{maior} pessoas;\033[m\n'
      f'Menor idade: \033[1m{menor} pessoas.\033[m')
