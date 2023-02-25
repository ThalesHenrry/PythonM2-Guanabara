# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
# O usuário deverá informar a quantidade de CDs e o valor para em cada um.

p = 1
c = 0
soma = 0
lista_cd = []
quantidade_cd = int(input('Quantidade de CD: '))

while quantidade_cd > c:
    valor = float(input(f'Valor {p}º CD: R$ '))
    lista_cd.append(valor)
    p += 1
    quantidade_cd -= 1

for lista_cd in lista_cd:
    soma += lista_cd

print(f'A média gasta por Cd é de R${soma/(p-1):.2f}')
print(f'E a soma total de gastos com Cds é R${soma:.2f}')
