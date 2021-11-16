""" count - Itertools """

from  itertools import count
from typing import Container

""" contador = count(start=5, step=-1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 100 or valor <= -10: 
        break """

contador = count()

""" lista = ['Luiz', 'João', 'Maria']
lista = zip(contador, lista)
print(list(lista)) """