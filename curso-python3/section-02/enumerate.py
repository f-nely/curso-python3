txt = 'O Brasil é penta.'
lista = txt.split()
print(lista)

print('-=' * 10)
for indice, valor in enumerate(lista):
    print(f'{indice} - {valor}')

lista2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print('-=' * 10)
for i in lista2:
    print(i)

print('-=' * 10)
for i in lista2:
    print(i[0], i[1])

lista3 = [
    [0, 'Luiz'],
    [1, 'Grace'],
    [2, 'James']
]

print('-=' * 10)
for i, valor in lista3:
    print(i, valor)

names = ['Luiz', 'Diana', 'Steve']

print('-=' * 10)
for i, valor in enumerate(names):
    print(i, valor)

n1, n2, n3 = names
print('-=' * 10)
print(n2)
