"""
Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
"""

num = int(input('Digite um número inteiro para calcular o fatorial: ')) 

if num < 0:
    print('O fatorial não é definido para números negativos.')
elif num == 0 or num == 1:
    print(f'O fatorial de {num} é 1.')
else:
    fatorial = 1
    for i in range(2, num + 1):
        fatorial *= i
    print(f'O fatorial de {num} é {fatorial}.')

    