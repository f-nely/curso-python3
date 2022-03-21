num = input('Digite um número: ')

if not num.isdigit():
    print('Por favor, digite um número inteiro.')
else:
    num = int(num)
    if num % 2 == 0 and num != 0:
        print(f'O {num} é par.')
    elif num == 0:
        print('Número igual a zero.')
    else:
        print(f'O {num} é ímpar.')
