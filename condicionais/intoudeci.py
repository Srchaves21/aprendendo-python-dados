#Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.#


num = float(input('Digite o seu número: '))
if num.is_integer():
    print('O número é inteiro.')
else:
    print('O número é decimal.')
