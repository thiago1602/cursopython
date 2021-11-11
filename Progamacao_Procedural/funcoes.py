# são criadas para não repetirmos as coisas

def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    return f'{msg} {nome}'


variavel = saudacao()

print(variavel)
