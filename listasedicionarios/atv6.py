#Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.#

data = {'dia': list(range(1, 32)),
        'mes': list(range(1, 13)),
        'ano': list(range(1900, 2027))
}

print("###AVALIADOR DE DATAS###")

while True:
    dia = int(input("Digite o dia : "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    if dia in data['dia'] and mes in data['mes'] and ano in data['ano']:
        print("Data válida.")
        break
    else:
        print("Data inválida. Digite uma data válida.")