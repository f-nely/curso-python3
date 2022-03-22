frase = 'Learning Python 3'
tamanho_frase = len(frase)
print(tamanho_frase)
print('-' * 20)

cont = 0
nova_string = ''
while cont < tamanho_frase:
    # print(frase[cont], cont)
    nova_string += frase[cont]
    print(nova_string)
    cont += 1
