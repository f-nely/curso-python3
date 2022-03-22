# j = 0
# while j <= 10:
#     print(j, end=' ')
#     j += 1
# print('- FIM')

# x = 0
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f'({x},{y})')
#         y += 1
#
#     x += 1
#
# print('Acabou!')

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    op = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Por favor, digite números inteiros.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        if num2 != 0:
            print(num1 / num2)
    else:
        print('Operação inválida.')

    resp = input('Deseja sair? [S/N] ').upper()

    if resp == 'S':
        break
