"""
Formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

# num1 = 10
# num2 = 3
# divisao = num1 / num2
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

# nome = 'Luiz Otávio'
# print(f'{nome:s}')
# print(f'{nome:#^50}')
# nome_formatado = '{:@>50}'.format(nome)
# nome_formatado = '{n}, {n}, {n}, {n}'.format(n=nome)
# print(nome_formatado)
nome = 'Otávio'
sobrenome = 'Miranda'
# nome_formatado = '{0}'.format(nome, sobrenome)
nome_formatado = '{0:-^30}'.format(nome, sobrenome)
print(nome_formatado)

# num1 = 1
# print(f'{num1:0>10}')
# num2 = 1150
# print(f'{num2:0>10}')
# print(f'{num2:0^10}')
# print(f'{num2:0<10}')
# print(f'{num2:.2f}')
# print(f'{num2:0>10.2f}')
