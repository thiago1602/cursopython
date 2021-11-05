#Operadores relacionais == > >= < <= !=

# num_1 = 2
# num_2 = 0
#
# expressao = (num_1 > num_2)
#
# print(expressao)

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} NÃO pode pegar o emprestimo')