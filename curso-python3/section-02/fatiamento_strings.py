"""
Manipulando strings
* string índices
* fatiamento de strings [início:fim:passo]
* funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""

# posi  [01234567]
texto = 'Python 3'
# nega  [87654321]
print(texto[2])
print(texto[7])
print(texto[-1])
print(texto[2:6])
print(texto[:6])
print(texto[7:])
print(texto[-8])
print(texto[-8:-2])

texto2 = 'Python s2'
print(texto2[:-1])
print(texto2[:-2])
print(texto2[0:6:2])
print(texto2[0::2])
print(texto2[0::3])

url = 'www.google.com.br/'
print(url[:-1])
