#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.#

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
restodiv = num1 % num2

print(f'O resto da divisão dos números selecionados é: {restodiv}')