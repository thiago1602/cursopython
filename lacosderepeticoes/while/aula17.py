# enquanto for ... faça
# while True:
# nome = input("Qual o seu nome?")
#   print(f'Olá{nome}!')

#print('não será executada')

x = 0
# while x < 10:
# if x == 3:
#       x = x + 1
#       break  # continue continua até 10 e pula o 3
# break vai até 2

# print(x)
#x = x + 1

# print('Acabou')

x = 0  # coluna
while x < 10:
    y = 0  # linha

    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1  # x = x +1

print('Acabou')
