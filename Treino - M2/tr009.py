# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
# varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

soma = 0
lista_idade = []
c = 1
qtd_pessoas = int(input('Quantidade de pessoas para a pesquisa? '))

while (c < qtd_pessoas + 1):
    idade = int(input(f'Qual a idade da {c} pessoa?'))
    lista_idade.append(idade)
    c += 1

for lista_idade in lista_idade:
    soma += lista_idade
media = soma / qtd_pessoas

print('=-'*12)
print(f' \033[1mMedia das idades {media:.2f}\033[m')

if media > 0 and media <= 25:
    print(' Media da turma: \033[1;31mJovem\033[m')
elif media > 60:
    print(' Media da turma: \033[1;32mIdoso\033[m')
else:
    print(' Media da turma: \033[1;33mAdulto\033[m')
