#Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).#

percent = int(input('Digite o percentual de crescimento da sua empresa: '))

if percent > 0:
    print(f'O percentual da empresa ta babado')
elif percent == 0:
    print(f'mona, MELHORE!!')
else:
    print(f'Mana MELHORE MUITO, pq ta babado forte!')