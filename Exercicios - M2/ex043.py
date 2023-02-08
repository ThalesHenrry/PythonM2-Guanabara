#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5: Abaixo do peso | 18.5 a 25: Peso ideal | 25 a 30: Sobrepeso | 30 a 40: Obesidade | +40: Obesidade Morbida

peso = float(input('Seu peso (Kg): '))
altura = float(input('Sua altura (M): '))
if altura.is_integer():
    altura = altura / 100
imc = peso / (altura**2)


if imc <= 18.5:
    status = '\033[1;31mAbaixo do peso\033[m'
elif imc < 25:
    status = '\033[1;32mPeso ideal\033[m'
elif imc < 30:
    status = '\033[1;33mSobrepeso\033[m'
elif imc < 40:
    status = '\033[1;31mObesidade\033[m'
else:
    status = '\033[1;31mObesidade Mórbida\033[m'

print(f'\033[1mSeu IMC: {imc:.1f}\033[m\n'
      f'\033[1mStatus:\033[m {status}')