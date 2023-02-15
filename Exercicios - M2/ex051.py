# Desenvolva um programa que leia o primeiro termo e a razao de uma (progressão aritmética).
# No final, mostre os 10 primeiros termo dessa progressão.


razao = int(input('Escolha a razão: '))
primeiro = razao
n = 10

ult = primeiro + (n-1)*razao
ult = ult+1

for c in range(primeiro, ult, razao):
    print(c)

print('fim')
