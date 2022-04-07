t1 = (1, 2, 3, 'a', 'Luiz Otávio')
print(type(t1), t1)
print(t1[2:])

t2 = 1,
print(type(t2))

t3 = 1, 2, 3, 4, 5
t4 = 6, 7, 8, 9, 10
t5 = t3 + t4
print(t5)

t6 = 1, 2, 'Luiz', 4, 5
n1, n2, n3, *_ = t6
print(n3)

t6 = (1, 2, 'Luiz', 4, 5) * 5
print(t6)
