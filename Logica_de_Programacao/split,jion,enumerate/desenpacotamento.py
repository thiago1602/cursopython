lista = ['Thiago', 'Joao', 'Maria', 1, 2, 3, 4, 5, 100]

n1, n2, n3, *outra_lista, ultimo_lista = lista
outra_lista, ultimo_lista, *n1, n2, n3 = lista

print(n1)
