#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5: Abaixo do peso | 18.5 a 25: Peso ideal | 25 a 30: Sobrepeso | 30 a 40: Obesidade | +40: Obesidade Morbida

peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso / (altura**2)

if imc <= 18.5:
    status = 'Abaixo do peso'
elif imc < 25:
    status = 'Peso ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'Seu IMC: {imc:.2f}\n'
      f'Status: {status}')