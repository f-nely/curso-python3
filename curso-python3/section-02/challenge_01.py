from datetime import date

name = 'Luiz'
age = 35
height = 1.80
weight = 80.5

year = date.today().year
year_birth = year - age

imc = weight / height ** 2

print(f'{name} tem {age} anos e {height} de altura e peso {weight}kg.')
print(f'O IMC de {name} é {imc:.2f}.')
print(f'{name} nasceu em {year_birth}.')
