# def hello_mundo():
#     return 'Hello world'
#
#
# def fuc2(funcao):
#     return funcao()
#
#
# print(fuc2(hello_mundo))

def func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def hi(nome):
    return f'Oi {nome}!'


def saudacao(nome, msg):
    return f'{msg} {nome}'


executando = func(hi, 'Luiz')
executando2 = func(saudacao, 'Luiz', msg='Good afternoon')
print(executando)
print(executando2)
