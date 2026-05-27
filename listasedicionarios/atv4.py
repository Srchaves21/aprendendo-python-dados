#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.#

lista = []
lista_teste = list(range(1,11))

for itens in range(1,6):
    lista.append(itens)
print(lista)  

lista.reverse()
print(f'A ordem inversa dos numeros na lista é:{lista}')

