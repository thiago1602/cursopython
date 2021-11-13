""" zip - Unindo iteraveis
zip_longest - Itertools """

from itertools import count, zip_longest

###código

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']

#código

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

for valor in cidades_estados:
    print(valor)