# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações

c = 0
while c == 0:
    nome = input('Seu nome: ').lower().split()
    senha = input('Senha: ').lower().split()
    if senha == nome:
        print('Senha não pode ser igual ao nome!')
    else:
        print('Cadastro feito com Sucesso!')
        c = 1

