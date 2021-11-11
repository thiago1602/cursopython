""" variavel = 'valor'

def func():
    print(variavel)

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()

func2()

print(variavel) """

def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)