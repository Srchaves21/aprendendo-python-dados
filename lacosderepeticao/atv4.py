"""
Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
"""

temperaturas = []


while True:
    temp = float(input("Digite a temperatura em Celsius (ou -273 para encerrar): "))
    if temp == -273 :
        print('Você escolheu parar!')
        break
    else: 
        temperaturas.append(temp)
if len(temperaturas) == 0:
    print('Nenhuma temperatura valida foi inserida')
else:
    media = sum(temperaturas) / len(temperaturas)
    print(f'A média das temperaturas selecionadas é: {media:.2f} °C')




"""while True:
    temp = float(input("Digite a temperatura em Celsius (ou -273 para encerrar): "))
    if temp == -273:
        break
    temperaturas.append(temp)

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"A média das temperaturas é: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi inserida.")"""