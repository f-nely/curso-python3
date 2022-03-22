"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, etc..
min, max
range
"""

names = ['Grace Hopper', 'Guido Von Rossum', 'James Gosling']
print(names)

lista = ['A', 'B', 'C', 'D', 'E']
print(lista[0])
print(lista[1:4])
print(lista[:3])
print(lista[2:])
print(lista[-1])
print(lista[::2])
print(lista[::-1])
print('-' * 30)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# print(l3)
# l1.extend(l2)
# l2.append(7)
# l2.insert(0, 7)
# l1.insert(3, 'apple')
# print(l1)
# l1.pop()
# print(l1)
# print(l2)

# l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l3)
# del l3[3:5]
# print(l3)
# print(min(l3))
# print(max(l3))
# l3 = []
# for i in range(1, 10):
#     l3.append(i)
# print(l3)
# l4 = list(range(0, 100, 8))
# print(l4)
# s = 0
# for i in l4:
#     s += i
# print(s)
# l5 = ['string', True, 10, -20.4]
# for i in l5:
#     print(f'O tipo do elemento é {type(i)} e seu valor é {i}')

secreto = 'perfume'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz, a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    # print(secreto_temporario)
    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
