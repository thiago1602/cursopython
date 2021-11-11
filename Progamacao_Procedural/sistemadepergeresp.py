
perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1','b':'4','c':'5',},
        'resposta_certa' : 'b',
    }, 
    'Pergunta 2':{
        'pergunta': 'Quanto é 4*2?',
        'respostas': {'a': '4','b':'10','c':'8',},
        'resposta_certa' : 'c',
    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 4*5?',
        'respostas': {'a': '4','b':'10','c':'20',},
        'resposta_certa' : 'c',
    },
    'Pergunta 4':{
        'pergunta': 'Quanto é 8*3?',
        'respostas': {'a': '24','b':'10','c':'8',},
        'resposta_certa' : 'a',
    },'Pergunta 5':{
        'pergunta': 'Quanto é 8*2?',
        'respostas': {'a': '4','b':'16','c':'8',},
        'resposta_certa' : 'b',
    },
}

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposa_usuario = input('Sua resposta:  ')

    if resposa_usuario == pv['resposta_certa']:
        print('EHHHHHHHHHHH!!!! Você acertou!!!1')
        respostas_certas += 1
    else:
        print('IXIIIIIIIII!!!! Você errou')
    print()

qtd_perguntas = len(perguntas)
porcentagem_erro = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi de {porcentagem_erro}%')