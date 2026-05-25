"""
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
"""
quant_usuarios = 15
contador = 0

while contador < quant_usuarios:
    estrelas = int(input('Digite a sua avaliação em um numero de 1 a 5 estrelas: '))
    if 1 <= estrelas and 5 >= estrelas:
        contador += 1
        print('Obrigado por avaliar!')
    else:
        print('Digite um número valido!')  
print('Obrigado por avalairem!')