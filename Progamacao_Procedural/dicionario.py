import copy

d1 = {1:'a', 2:'b', 3:'c', 'd' : ('Thiago', 'Moraes')}
v= d1.copy()

v[1] = 'Thiago'
v['d'] = ('Thiago', 'Moraes')

print(d1)
print(v)
#chaves tem que ser unicas,

""" d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'valor da nova chave'

print(d1['chave1']) """

""" d1 = {

    'str':'valor',
    123:'Outro valor',
    (1,2,3,4) : 'Tupla'
} """

#encontrar valores 
""" print('str' in d1)
print('str' in d1.keys)
print('valor' in d1.values)
 """
""" print(len(d1)) """

""" for k in d1.items():
    print(k[0], k[1])
 """
#dicionarios dentro de
""" clientes = {
    'cliente1' :{
        'nome' : 'Thiago',
        'sobrenome' : 'Moraes'

    },
    'cliente2' :{
        'nome' : 'Joao',
        'sobrenome' : 'Silva'

    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}') """