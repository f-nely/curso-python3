first_name = str(input('Digite seu primeiro nome: '))

tamanho = len(first_name)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande.')
