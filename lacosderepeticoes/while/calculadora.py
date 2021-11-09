while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digita um operador: ')
    sair = input('Deseja sair [s]im ou [n]ão: ')

    if sair == 's':
        break
    if not num1.isnumeric() or num2.isnumeric():
        print('Você precisa digitar um numero.')

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Operador inválido')
