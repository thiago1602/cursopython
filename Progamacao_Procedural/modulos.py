# https://docs.python.org/3/py-modindex.html

# É UM OUTRO ARQUIVO PY, QUE TENHA ARQUIVOS PY
# from random import randint
#
# for i in range(60):
#     print(randint(0,10))

import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)

    print(__name__)

