# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os epaço
#De tras pra frente a frase continua igual

frase = input('Escreva uma frase: ').split()
frase = ''.join(frase).lower()

if frase[::-1] == frase:
    print(
        f'É Palíndromo!'
    )
else:
    print(
        f'Não é Palíndromo!'
    )
