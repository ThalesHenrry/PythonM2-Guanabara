from datetime import date

# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alista ao serviço militar | Se é a hora de se alistar | Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

sexo = str(input('Sexo\n'
                 '[1] Masculino\n'
                 '[2] Feminino\n'
                 'R: '))
if sexo == '2':
    print('\033[1;31mNão é obrigado o alistamento militar ao sexo Feminino!\033[m')
else:
    nasc = int(input('Digite o ano do seu nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc

    if idade < 18:
        print('Ainda irá se alistar ao Serviço Militar!\n'
              f'\033[1;43mFalta:\033[m {18 - idade} anos.\n'
              f'Ano de alistamento: {nasc + 18}')
    elif idade > 18:
        print('\033[1;41mALERTA:\033[m já Passou da hora de se alistar ao Serviço Militar!\n'
              f'Atraso: {idade - 18} anos.\n'
              f'Ano de alistamento: {nasc + 18}')
    else:
        print('\033[1;42mAVISO:\033[m Está na hora de se alistar ao Serviço Militar\n'
              f'Ano de alistamento: {nasc + 18}')
