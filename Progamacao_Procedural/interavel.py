#interaveis
#lists, tuples, str -> Sequences -> Interavel

""" lista = [0,1,2,3,4,5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__')) """

""" import sys
import time

def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
g = gera()
print(g) """


nome = 'Thiago Moraes'
iterador = iter(nome)

""" for letra in nome:
    print(letra)

print('#' * 80)

for letra in nome:
    print(letra)

print(nome)
 """
