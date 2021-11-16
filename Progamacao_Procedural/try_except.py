try:
    a = {}
    try:
        a = 1/0
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele')
except IndexError as erro:
    print('Erro de indice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso')
    print(a)
finally:
    print('Finalmente')
print('Continuar')