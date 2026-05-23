"""
Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”. 
"""
#Primeiro Caso#
nome_usuario = input('Digite seu nome:')
print(f'Óla, {nome_usuario}!')

#Segundo Caso#
nome = input('Digite sua seu nome: ')
idade = input('Digite sua idade: ')
print(f'Ola {nome}, você tem: {idade} anos!')

#Terceiro Caso#
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura em metros: ')

print(f'Olá {nome}, você tem {idade} anos e mede {altura}m')