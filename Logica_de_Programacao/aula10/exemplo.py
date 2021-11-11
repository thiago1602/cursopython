usuario = input('Nome do usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'thiago'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você esta logado no sistema')
else:
    print('Usuário ou senha invalido')