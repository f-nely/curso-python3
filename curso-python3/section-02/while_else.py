cont = ac = 1
while cont <= 10:
    print(cont, ac)

    if cont > 5:
        break
    ac += cont
    cont += 1
else:
    print('Cheguei no else.')
print('Isso será executado.')
