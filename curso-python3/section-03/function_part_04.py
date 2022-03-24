variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel
    variavel = 'outro valor'
    print(variavel)


func()
func2()
print(variavel)
