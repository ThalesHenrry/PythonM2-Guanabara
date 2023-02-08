from random import choice

# Crie um programa que faça o computador jogar Jokenpô com você.

print('-=' * 20)
print('              \033[1;97mJOKEMPO\033[m')
print('-=' * 20)

lista = ['Pedra', 'Papel', 'Tesoura']
sorte = choice(lista)
escolha = input('- Pedra\n'
                '- Papel\n'
                '- Tesoura\n'
                ' Escolha: \n').capitalize()

print('        \n')

if escolha == 'Pedra' and sorte == 'Tesoura':
    status = 'Você ganhou'
elif escolha == 'Papel' and sorte == 'Pedra':
    status = 'Você ganhou'
elif escolha == 'Tesoura' and sorte == 'Papel':
    status = 'Você ganhou'
elif (escolha == 'Pedra' and sorte == 'Pedra') or \
        (escolha == 'Papel' and sorte == 'Papel') or \
        (escolha == 'Tesoura' and sorte == 'Tesoura'):
    status = 'Empate!'
else:
    status = 'Você perdeu'

print(
    f'Status: \033[1m{status}\33[m\n'
    f'Você: {escolha} X Computador: {sorte}'
)
