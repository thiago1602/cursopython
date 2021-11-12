l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1] # cada elemento da l1 na variavel

print(l2)

exemplo2 = [v * 2 for v in l1] #cada elemento x 2
print(exemplo2)

exemplo3 = [(v, v2) for v in l1 for v2 in range(3)]
print(exemplo3)

l2 = ['Thiago', 'Maria', 'Bruna']
exemplo4 = [v.replace('a', '@').upper() for v in l2]#substitui o a por @
print(exemplo4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y,x) for x, y in tupla] 
ex5 = dict(ex5)
print(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v %2 ==0] #todos os numeros divisiveis por 2
print(ex6)