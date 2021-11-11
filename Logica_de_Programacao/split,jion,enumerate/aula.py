# split, faz separacao da frase com ,
string = "O Brasil é o pais do futebol, o Brasil é penta"
lista = string.split(' ')
lista2 = string.split(',')

for valor in lista:
    # conta qtas x a palavra apareceu na frase
    print(f'A palavra {valor} apareceu {lista.count(valor)} x na frase')

palavra = ''
contagem = 0
for valor in lista:
    qtde_vezes = lista.count(valor)

    if qtde_vezes > contagem:
        contagem = qtde_vezes
        palavra = valor

    # conta qtas x a palavra apareceu na frase
    print(
        f'A palavra que apareceu mais vezes é {palavra} apareceu {contagem} x')

# join
string2 = 'O brasil é penta.'
lista3 = string2.split(' ')
string3 = ','.join(lista3)

print(string2)
print(lista3)
print(string3)

# enumerate

string4 = 'O brasil é exa'
lista4 = string4.split(' ')

for indice, valor in enumerate(lista4):
    print(indice, valor, lista4[indice])

lista5 = ['Thiago', 'Joao', 'Maria']
n1, n2, n3 = lista5

print(n2)
for v in lista5:
    print(v)
