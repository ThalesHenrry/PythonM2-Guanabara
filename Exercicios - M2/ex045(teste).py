from random import choice
from time import sleep
import emoji

# Crie um programa que faça o computador jogar Jokenpô com você.

print('-=' * 20)
print('              \033[1;97mJOKEMPO\033[m')
print('-=' * 20)

lista = ['Pedra', 'Papel', 'Tesoura']
sorte = choice(lista)
escolha = input('[1] Pedra\n'
                '[2] Papel\n'
                '[3] Tesoura\n'
                'Escolha:  ')

print('        ')

print('\033[1mjO', end='')
sleep(1)
print('KEM', end='')
sleep(1)
print('PÔ!!!\033[m')

print('-'*20)
if escolha == '1' and sorte == 'Tesoura':
    status = 'Você ganhou'
elif escolha == '2' and sorte == 'Pedra':
    status = 'Você ganhou'
elif escolha == '3' and sorte == 'Papel':
    status = 'Você ganhou'
elif (escolha == '1' and sorte == 'Pedra') or \
        (escolha == '2' and sorte == 'Papel') or \
        (escolha == '3' and sorte == 'Tesoura'):
    status = 'Empate!'
else:
    status = 'Você perdeu'

if escolha == '1':
    aposta = 'Pedra'
if escolha == '2':
    aposta = 'Papel'
if escolha == '3':
    aposta = 'Tesoura'
if (escolha == '1' and sorte == 'Pedra'):
    aposta = 'Pedra'
if (escolha == '2' and sorte == 'Papel'):
    aposta = 'Papel'
if (escolha == '3' and sorte == 'Tesoura'):
    aposta = 'Tesoura'

print(
    f'Status: \033[1m{status}\33[m\n'
    f'Você: {aposta} X Computador: {sorte}'
)

#IMCOMPLETO: FUNCIONAL, AINDA FALTA AGUNS COMPLEMENTOS 08/02/23