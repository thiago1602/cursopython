""" def funcao(var):
    return var


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor. ')
 """


""" def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)
print(divide)

if divide:
    print(divide)
else:
    print('Conta inválida') """


def dumb():
    return [1, 2, 3, 4, 5]


var = dumb()
print(var, type(var))


def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f))


def dumb():
    return ('Thiago', 'Moraes')


var = dumb()

print(var[1], type(var))
