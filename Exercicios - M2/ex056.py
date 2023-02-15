# Desenvolva um programa que leia, nome, idade e sexo de 4 pessoas. Mostre no final:
# Media de idade do grupo | nome do homem mais velho | quantas mulher tem menos de 21.

media = 0
velho = 0
mulher = 0

for c in range(0, 4):
    nome = input("Nome: ")
    idade = int(input('Idade: '))
    sexo = input("Sexo:[1] Masculino\n"
                 "     [2] Feminino\n"
                 "      R: ")
    print('')
    media += idade / 4
    if idade > velho and sexo == '1':
        velho = idade
        homem_velho = nome
    if idade < 20 and sexo == '2':
        mulher += 1

print(f'- A média de idade do grupo: \033[1m{media}\033[m')
print(f'- O homem mais velho é: \033[1m{homem_velho.capitalize()}\033[m\n'
      f'sua idade: \033[1m{velho} anos\033[m')
print(f'- Mulheres com menos de 20 anos: \033[1m{mulher}\033[m')