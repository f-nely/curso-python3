def funcao(var):
    return var


# funcao('Valor que eu quero')
variavel = funcao('Valor que eu quero')
print(variavel)


def divisao(n1, n2):
    if n2 == 0:
        return

    return round(n1 / n2, 1)


divide = divisao(8, 3)
if divide:
    print(divide)
else:
    print('Denominador não pode ser zero.')


def f(var1):
    print(var1)


def dumb():
    return f


print(type(f))
# varr = dumb()('E colocar o meu valor aqui.')
