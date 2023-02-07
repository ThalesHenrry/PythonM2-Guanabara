#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai pergunta o valor da casa, o salário do comprador e em qunatas anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não poder exceder 30% do salário ou então o empréstimo sera negado.

print(
    f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    f'        \033[1;45mLIBERAÇÃO DE EMPRÉSTIMO\033[m \n'
    f'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
)

nome = str(input('Qual o seu nome: '))
valor_casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Seu salário: R$'))
parcela = int(input('Quantidade de anos a pagar: '))

mensalidade = (12 * parcela)
mes = valor_casa / mensalidade
limite = (salario*30/100) + salario

if mes > limite:
    print(
        f'\033[1;41mEMPRÉSTIMO NEGADO!\033[m\n'
        f'* A mensalidade calculada, ultrapassa o limite permitido de 30% em cima do seu salário.\n'
        f'Ficando no valor de \033[1mR${limite:.2f}\033[m'
    )
else:
    print(
        f'Senhor(a) \033[1;4m{nome}.\033[m\n'
        f'  O valor mensal de seu empréstimo é \033[1mR${mes:.2f} em {mensalidade:.0f}X\033[m\n'
    )

