#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5; Reprovado | Entre 5 e 6.9; Recuperação | Superior a 7; Aprovado.

nome = str(input('Nome: '))
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    status = '\033[1;31mReprovado(a)\033[m'
elif media >= 7:
    status = '\033[1;32mAprovado(a)\033[m'
else:
    status = '\033[1;33mRecuperação\033[m'

print(
    f'Aluno(a): \033[1m{nome}\033[m.\n'
    f'Sua Média é {media:.2f}\n'
    f'Status: {status}.'
)

