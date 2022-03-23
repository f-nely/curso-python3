lista = [
    ['Edu', 'Ana', 'Luiz'],
    ['Diana', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]

enumerada = list(enumerate(lista))
print(enumerada)
print('-=' * 10)
print(enumerada[1][1][2])

print('-=' * 10)
for v1, v2 in enumerate(lista, 50):
    print(v1, v2)
