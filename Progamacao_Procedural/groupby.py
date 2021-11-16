from itertools import groupby, tee

alunos = [
    {
        'nome':'Thiago', 'nota':'A'
    },{
        'nome':'lAISSA', 'nota':'B'
    },{
        'nome':'Bruna', 'nota':'C'
    },{
        'nome':'Vitor', 'nota':'D'
    },{
        'nome':'Anderson', 'nota':'B'
    },{
        'nome':'Maria', 'nota':'C'
    }
]

ordena = lambda item: item['nota']
alunos.sort(key = ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupado in alunos_agrupados:
    va1,va2 = tee(valores_agrupado)
    print(f'Agrupamento:{agrupamento}')

    quantidade = len(list(valores_agrupado))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    for aluno in va1:
        print(aluno)
