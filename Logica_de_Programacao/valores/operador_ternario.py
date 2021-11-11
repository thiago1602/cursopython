logged_user = False

""" if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar' """

""" msg = 'Usuário logado.' if (logged_user) else 'Usuário precisa logar'
 """

idade = input('Qual a sua idade?')

if not idade.isnumeric():
    print('Digite apenas numeros')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

    print(msg)
