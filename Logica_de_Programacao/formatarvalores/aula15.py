num1 = 10
num2 = 3

divisao = num1 / num2

print(divisao)

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')


nome = 'Thiago de Moraes'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0<10}')

nome = 'Thiago de Moraes'
nome_formatado = '{:@>17}'.format(nome)
print(nome_formatado)

nome = 'Thiago de Moraes'
nome_formatado1 = '{n:0<20}'.format(n=nome)
print(nome_formatado1)

nome = 'thiago de Moraes'
nome = nome.ljust(20, '#')
print(nome.lower())
print(nome.upper())
print(nome.title())
