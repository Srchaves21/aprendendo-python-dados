"""
 Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para variação abaixo de -10%: corte de gastos.
"""

quant_vendas_2022 = float(input('Digite a quantidade de vendas em 2022: '))
quant_vendas_2023 = float(input('Digite a quantidade de vendas em 2023: '))

calculo_variacao = ((quant_vendas_2023 - quant_vendas_2022) / quant_vendas_2022) * 100

if calculo_variacao > 20:
    print('Bonificação para o time de Vendas!')
elif calculo_variacao <= 20 and calculo_variacao > 2:
    print('Pequena bonificação para o time de vendas')
elif calculo_variacao <= 2 and calculo_variacao > -10:
    print('Planejamento de políticas de incentivo às vendas.')
else:
    print('Corte de gastos')