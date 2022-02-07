#Listas, dicionarios
#Tuplas, strings
def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes1 = ['Thiago']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_de_clientes1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
cientes3 = lista_de_clientes(['Thiago'])

print(clientes1)
print(clientes2)