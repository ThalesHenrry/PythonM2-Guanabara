#Refaça p ex35 e acrescente o recurso de mostrar que tipo de triangulo será:
#Equilátero: todos os lado iguais
#Isóceles: dois lado iguais
#Escaleno: todos os lados diferentes

linha1 = float(input('Comprimento da 1º linha: '))
linha2 = float(input('Comprimento da 2º linha: '))
linha3 = float(input('Comprimento da 3º linha: '))

prova1 = (linha1 > abs(linha2-linha3)) and (linha1 < abs(linha2+linha3)) and \
         (linha2 > abs(linha1-linha3)) and (linha2 < abs(linha1+linha3)) and \
         (linha3 > abs(linha1-linha2)) and (linha3 < abs(linha1+linha2))

print('    \n')

if prova1 == True:
    print(
        f'Possivel formar um Triângulo!'
    )
else:
    print(
        f'Impossivel formar um Triângulo!'
    )

if linha1 and linha2 and linha3 == linha1 and linha2 and linha3:
    print('- Triângulo Esquilátero')
elif linha1 != linha2 and linha1 != linha3 and linha3 != linha2:
    print('- Triângulo Escaleno')
else:
    print('- Triângulo Isóceles')