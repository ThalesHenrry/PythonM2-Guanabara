from datetime import date

#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim| 14 anos: Infantil| 19 anos: Junior| 20 anos: Sênior| Acima: Master

nasci = int(input('Ano de nascimento: '))
idade = date.today().year - nasci

if idade <= 9:
    classe = 'Mirim'
elif idade <= 14:
    classe = 'Infantil'
elif idade <= 19:
    classe = 'Junior'
elif idade <= 20:
    classe = ' Sênior'
else:
    classe = 'Master'

print(
    f'Sua Categoria é {classe}!'
)

