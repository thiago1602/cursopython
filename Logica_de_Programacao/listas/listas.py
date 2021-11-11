#          0   1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#       - 5    4    3    2    1

lista[5] = 'Qualquer outra coisa'
print(lista[1:4])
print('-------------------------')
print(lista[:3])
print('-------------------------')
print(lista[0])
print('-------------------------')
print(lista[::2])  # começo, fim e salto
print('-------------------------')
print(lista[::-1])
print('-------------------------')

#l1 = [1, 2, 3]
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#l3 = l1 + l2
# l1.extend('a')
l2.insert(0, 'Banana')
print(l2)
del(l2[0])
print(l2)


# print(l2[3])

# l2.append('b')

# print(l1)
# print(l2)
# print(l3)

print('-----------------------------')

#l3 = ['String', True, 10, -20.5]
# for elem in l3:
# print(f'O tipo de elem é {type}')

# forca
secreto = 'perfume'
digitada = []
chances = 3
while True:
    if chances <= 0:
        print('Você perdeu')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale,  digite apenas uma letra')
        continue

    digitada.append(letra)

    if letra in secreto:
        print(f'UHUUL, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Aff: a letra"{letra}" nã existe na palavra secreta')
        digitada.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

        if secreto_temporario == secreto:
            print(
                f'Que legal,VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances')
        print()
