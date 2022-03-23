my_tuple = ('John', 'Peter', 'Vicky')
x = '#'.join(my_tuple)
print(x)

text = ['Python', 'is', 'a', 'programming', 'language']
print(text)
print(type(text))
# join elements of text with space
print(' '.join(text))
print(type(' '.join(text)))

num_list = ['1', '2', '3', '4']
print(', '.join(num_list))

s1 = 'abc'
s2 = '123'

print('s1.join(s2):', s1.join(s2))

frase = 'O Brasil é penta.'
lista = frase.split()
frase2 = ', '.join(lista)

print('-=' * 10)
print(frase)
print(lista)
print(frase2)
