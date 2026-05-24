# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.#

carro1ano = 10000000000
carro2ano = 10000000
carro3ano = 70000

if carro1ano > carro2ano and carro1ano > carro3ano:
    print("O valor mais alto é do primeiro ano: R$", carro1ano)
elif carro2ano > carro1ano and carro2ano > carro3ano:
    print("O valor mais alto é do segundo ano: R$", carro2ano)
else:    print("O valor mais alto é do terceiro ano: R$", carro3ano)