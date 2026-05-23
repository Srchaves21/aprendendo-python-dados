nome = "Juliano floss"
nota = 8.5
ano = 2027

#___________________________%variavel_________________________________________________#
print('Nome do aluno: %s' %nome)
print('Nota do aluno: %.2f' %nota)
print('Ano de matricula: %d' %ano)

#___________________________.Format____________________________________________________#

print('Nome do aluno é: {}'.format(nome))
print('O nome dele é: {}, ele tem q nota: {} e entrou em {}'.format(nome,nota,ano))

#_____________________f'string'__mais utilizado e legivel_______________________________#

print(f'O nome do aluno é: {nome}, ele tirou a nota: {nota}, e adentrou a instituição no ano de: {ano}.')

#_____________________\n: utilizado para pular linha_______________________________________#

print('eu sabia que estava errado \n mesmo assim continuei incentivando a ideia!')

#_____________________\t: adiciona tabulação, tipo um TAB__________________________________#

print('eu sabia que estava errado \t mesmo assim continuei incentivando a ideia!')