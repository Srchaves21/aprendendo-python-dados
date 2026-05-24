#Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.#

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

qualoperacao = input('Digite qual operação quer realizar: "A" para Adição, "S" para Subtração, "M" para multiplicação ou "D" para divisão.').upper()

adicao = num1 + num2
subtracao = num1 - num2
multi = num1 * num2
divi = num1 / num2



if qualoperacao == 'A':
    print(f'Esse é seu resultado: {adicao} ')
    if adicao % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar.')
    if adicao > 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if adicao.is_integer():
        print('O resultado é inteiro.')
    else:
        print('O resultado é decimal.')
elif qualoperacao == 'S':
    print(f'Esse é seu resultado: {subtracao}')
    if subtracao % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar.')
    if subtracao > 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if subtracao.is_integer():
        print('O resultado é inteiro.')
    else:
        print('O resultado é decimal.')
elif qualoperacao == 'M':
    print(f'Esse é seu resultado: {multi}')
    if multi % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar.')
    if multi > 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if multi.is_integer():
        print('O resultado é inteiro.')
    else:
        print('O resultado é decimal.')
elif qualoperacao == 'D':
    print(f'Esse é seu resultado: {divi}')
    if divi % 2 == 0:
        print('O resultado é par.')
    else:
        print('O resultado é ímpar.')
    if divi > 0:
        print('O resultado é positivo.')
    else:
        print('O resultado é negativo.')
    if divi.is_integer():
        print('O resultado é inteiro.')
    else:
        print('O resultado é decimal.')
else:
    print('Digite uma operação Valida!')