#Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.#

produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))

if produto1 < produto2 and produto1 < produto3:
    print("O produto mais barato é o primeiro produto: R$", produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("O produto mais barato é o segundo produto: R$", produto2)
else:    print("O produto mais barato é o terceiro produto: R$", produto3)