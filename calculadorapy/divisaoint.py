#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.#

num1 = int(input('Digite o numerador: '))
num2 = int(input('Digite o denominador (não pode ser zero): '))

divisaoint = num1 // num2
print(f'O resultado da divisão inteira é: {divisaoint}')