# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     return nome, a6
#
#
# var = func(1, 2, 3, 4, 5, nome='Luiz', a6='5')
# print(var)

def func(*args, **kwargs):
    print(args)
    # print(kwargs['nome'], kwargs['sobrenome'])
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe.')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=31)
