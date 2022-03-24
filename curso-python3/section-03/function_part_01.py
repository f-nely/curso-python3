def gretting():
    return 'Good evening!'


print(gretting())


def saudacao(msg='Olá', nome='usuário'):
    return f'{msg} {nome}'


print('-=' * 10)
print(saudacao())
print(saudacao(nome='Zé'))
print(saudacao(nome='Xande', msg='Hola que tal'))
print(saudacao('Hello', 'Grace Hopper'))
print(saudacao('Hey', 'Otávio'))
