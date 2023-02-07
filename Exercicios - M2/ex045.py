from random import choice

#Crie um programa que faça o computador jogar Jokenpô com você.

lista = ['Pedra', 'Papel', 'Tesoura']
sorte = choice(lista)
escolha = input('[1] Pedra\n'
                '[2] Papel\n'
                '[3] Tesoura\n'
                'Escolha: ')


if sorte == 'Pedra' and escolha == 3:
    escolha = 'Tesoura'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ]\n ' 
        'VOCÊ PERDEU!'
    )
elif sorte == 'Tesoura' and escolha == 1:
    escolha = 'Pedra'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ]\n ' 
        'VOCÊ GANHOU!'
    )
elif sorte == 'Papel' and escolha == 1:
    escolha = 'Pedra'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ]\n ' 
        'VOCÊ PERDEU!'
    )
elif sorte == 'Pedra' and escolha == 2:
    escolha = 'Papel'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ]\n ' 
        'VOCÊ GANHOU!'
    )
elif sorte == 'Tesoura' and escolha == 2:
    escolha = 'Papel'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ\n '
        'VOCÊ PERDEU!'
    )
else:
    escolha = 'Tesoura'
    print(
        f'[COMPUTADOR] {sorte} X {escolha} [VOCÊ]\n '
        'VOCÊ GANHOU!'
    )