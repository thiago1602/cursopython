variavel = ['Thiago de Moraes', 'Laissa Costa', 'Bruna Santos']

""" for valor in variavel:
    print(valor)
    continue
    print(valor) """

for valor in variavel:
    print(valor)
    if valor.lower().startswith('l'):
        continue
else:
    print('Não existe uma palavra que comeca com T')
