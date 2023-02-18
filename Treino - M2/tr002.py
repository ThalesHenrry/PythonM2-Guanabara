# 26 Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
eleitor1 = 'Gabiru da Silva'
g = 0
eleitor2 = 'Selena Gomes'
s = 0
eleitor3 = 'Faustão'
f = 0

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

    # print(f'G:{g}\n'
    #       f'S:{s}\n'
    #       f'F:{f}')

print('=======RESULTADO=======')

# CAMPEÃO
camp = g
if g > s and f:
    camp = eleitor1
elif s > g and f:
    camp = eleitor2
else:
    camp = eleitor3

# ULTIMO
ult = g
if g < s and f:
    ult = eleitor1
elif s < g and f:
    ult = eleitor2
else:
    ult = eleitor3

# VICE
vice = g
if camp == eleitor1 and ult == eleitor3:
    vice = eleitor2
elif camp == eleitor2 and ult == eleitor3:
    vice = eleitor1
else:
    vice = eleitor3

# RESULTADO CAMPEÃO
if camp == eleitor1:
    print(f'CAMPEÃO: {camp} | VOTOS {g} ')
elif camp == eleitor2:
    print(f'CAMPEÃO: {camp} | VOTOS {s} ')
else:
    print(f'CAMPEÃO: {camp} | VOTOS {f} ')

# RESULTADO VICE
if vice == eleitor1:
    print(f'VICE: {vice} | VOTOS {g} ')
elif vice == eleitor2:
    print(f'VICE: {vice} | VOTOS {s} ')
else:
    print(f'VICE: {vice} | VOTOS {f} ')

# RESULTADO ULTIMO
if ult == eleitor1:
    print(f'ULTIMO: {ult} | VOTOS {g} ')
elif ult == eleitor2:
    print(f'ULTIMO: {ult} | VOTOS {s} ')
else:
    print(f'ULTIMO: {ult} | VOTOS {f} ')
