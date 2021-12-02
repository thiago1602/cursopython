# file = open('abc.txt', 'w+') #ler e escrever no arquivo
# file.write('Linha 1 \n')
# file.write('Linha 2 \n')
# file.write('Linha 3 \n')
# file.write('Linha 4 \n')
# file.write('Linha 5 \n')
#
# file.seek(0, 0)
# print('Lendo Linhas: ')
# print(file.read())
# print('=================')
# #lendo linha por linha
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
#
# print('===================')
# file.seek(0, 0)
# print(file.readlines())
# file.close()

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0) #le a linha escrita
#     print(file.read())

# import os
# os.remove('abc.txt')

#criando um arquivo json
import json

d1 = {
    'Pessoa1': {
        'nome': 'Thiago',
        'idade': 26,
    },
    'Pessoa2': {
        'nome': 'Laissa',
        'idade': 19,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
