#Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.#

letra = str(input('Escolha uma letra do alfabeto maiuscula ou minuscula: '))
vogal = ["a","A","e","E","i","I","o","O","u","U"]
if letra in vogal:
    print('Essa poha é vogal!')
else:
    print('Essa poha é consoante!')