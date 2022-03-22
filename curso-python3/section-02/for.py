word = 'python'

for letter in word:
    print(letter)

print('-' * 15)

for i, letter in enumerate(word):
    print(i, letter)

print('-' * 15)

for i in range(0, 11):
    print(i)

print('-' * 15)

for i in range(20, 9, -1):
    print(i)

print('-' * 15)

for i in range(0, 100, 7):
    print(i)

print('-' * 15)

new_string = ''
for letter in word:
    if letter == 't':
        new_string += letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
    else:
        new_string += letter
        
print(new_string)
