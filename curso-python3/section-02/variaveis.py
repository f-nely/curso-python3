nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade >= 18
peso = 80
imc = peso / (altura ** 2)

print(f'Nome: {nome}, idade: {idade}, altura: {altura}, é maior: {e_maior}')
print(f'{nome} tem {idade} anos de idade e seu imc é {round(imc, 2)}')
