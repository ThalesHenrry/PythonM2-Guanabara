# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

c = 0

while c == 0:
    nota = int(input('Uma nota de 0 á 10: '))
    if nota < 0 or nota > 10:
        print('Valor incorreto!')
    else:
        c = 1
        print('Obrigado!')
