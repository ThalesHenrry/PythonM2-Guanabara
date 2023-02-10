from time import sleep

# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de um segundo entre eles

for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('Feliz Ano Novooo!!!!')
