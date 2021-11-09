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
