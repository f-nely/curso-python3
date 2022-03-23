names = ['Luiz', 'Diana', 'Grace', 'Harris', 1, 2, 300]

# n1, n2, n3 = names
# print(n2)
# n1, n2, *outra_lista, ultimo_da_lista = names
# print(n1, n2, outra_lista)
# print(outra_lista)
# print(ultimo_da_lista)
# *outra_lista, n1, n2, n3 = names
# print(n1)
n1, n2, *_ = names
print(n1, n2)
