#26 Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
g=0
s=0
f=0

eleitores = int(input('Quantidade de eleitores: '))

for c in range(0, eleitores):
    print('Em quem deseja voltar?\n'
          '[1]Gabiru da Silva\n'
          '[2]Selena Gomes\n'
          '[3]Faustão')
    voto = int(input('Nº:'))
    if voto == 1:
        g += 1
    elif voto == 2:
        s += 1
    elif voto == 3:
        f += 1
    else:
        print('Voto Incorreto')

print('=======RESULTADO=======')

#CAMPEÃO
camp = g
if g > s and f:
    camp = g
elif s > g and f:
    camp = s
else:
    camp = f

#ULTIMO
ult = g
if g < s and f:
    ult = g
elif s < g and f:
    ult = s
else:
    ult = f

#VICE
vice = g
if camp == g or camp == s:
    vice = f
elif camp == s or camp == f:
    vice = g
else:
    vice = s

print(f'CAMPEÃO: {camp} ')

