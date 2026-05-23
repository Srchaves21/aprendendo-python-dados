#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.#

num1 = int(input('DIgite o primeiro numero: '))
num2 = int(input('Digite o segundo numero (não pode ser zero): '))
divisao = num1 / num2

print(f'A divisão dos numeros digitados é {divisao}')