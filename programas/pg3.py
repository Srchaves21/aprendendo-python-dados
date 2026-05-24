"""
Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
"""

quantidade = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input('Qual o tipo de combustivel? Selecione "E" para Etanol ou "D" para Diesel ').upper()

diesel = 2.0
desconto_diesel_menor = diesel*quantidade * 0.2
desconto_diesel_maior = diesel*quantidade * 0.4
valor_diesel_menor = diesel*quantidade - desconto_diesel_menor
valor_diesel_maior = diesel*quantidade - desconto_diesel_maior

etanol = 1.7
desconto_etanol_menor = etanol*quantidade * 0.3
desconto_etanol_maior = etanol*quantidade * 0.5
valor_etanol_menor = etanol*quantidade - desconto_etanol_menor
valor_etanol_maior = etanol*quantidade - desconto_etanol_maior


if tipo_combustivel == 'E':
    if quantidade <= 15:
        print(f'O valor a ser pago é {valor_etanol_menor}')
    else:
        print(f'O valor a ser pago é: {valor_etanol_maior}')
elif tipo_combustivel == 'D':
    if quantidade <= 15:
        print(f'O valor a ser pago é {valor_diesel_menor}')
    else:
        print(f'O valor a ser pago é: {valor_diesel_maior}')
else:
    print('Digite um número valido')