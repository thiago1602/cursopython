frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Qual letra deseja colocar maiúscula: ')

#Interação < - Alterar
while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
    #nova_string += frase[contador]
   # print(nova_string)


print(nova_string)
