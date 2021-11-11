""" def func(a1,a2,a3,a4,a5, nome=None, a6=None):
    print(a1,a2,a3,a4,a5, nome)
    return nome, a6

var = func(1,2,3,4,5, nome='Thiago', a6='5') """

""" def func(*args): #desenpacota a lista, sep separa a lista
    print(args)
    print(args[0]) #acessa o primeiro elemento da tupla
    #não pode alterar o elemento de uma tupla

lista = [1,2,3,4,5]
print(*lista, sep='+') """

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

lista = [1,2,3,4,5]
lista2=[10,20,30,40,50]
func(*lista, *lista2, nome='Thiago', sobrenome='Moraes', idade='26')

