txt = 'welcome to the jungle'
x = txt.split()
print(x)

nomes = 'Grace Hopper, James Gosling, Rasmus Lerdorf'
n = nomes.split(', ')
print(n)

sentence = 'hello, my name is Peter, I am 26 years old'
s = sentence.split(', ')
print(s)

fruits = 'apple#banana#cherry#orange'
f = fruits.split('#')
f1 = fruits.split('#', 1)
print(f)
print(f1)
