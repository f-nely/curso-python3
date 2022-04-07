mult = lambda n1, n2: n1 * n2
print(mult(2, 2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# lista.sort(key=lambda item: item[1])
# print(lista)
print(sorted(lista, key= lambda i: i[1]))
