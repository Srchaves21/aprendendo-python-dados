gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.#
new_gastos = []

for valores in gastos:
    if valores > 3000:
        new_gastos.append(valores)

print(f'O total de: {len(new_gastos)} compras foram realizadas acima de 3000!')

porcentagem = ( len(new_gastos) * 100) / len(gastos) 

print(f'A porcentagem quanto ao total de compras é: {porcentagem}%')

