#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5; Reprovado | Entre 5 e 6.9; Recuperação | Superior a 7; Aprovado.

nome = str(input('Nome: '))
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    status = 'Reprovado(a)'
elif media > 7:
    status = 'Aprovado(a)'
else:
    status = 'Recuperação'

print(
    f'Aluno(a): {nome}.\n'
    f'Sua Média é {media:.2f}\n'
    f'Status: {status}.'
)

