def greeting(msg, name):
    return f'{msg}, {name}!'


print(greeting('Good afternoon', 'Mario'))


def summ(num1, num2, num3):
    return num1 + num2 + num3


print(summ(11, 2, 5))


def aumento(valor, p):
    result = valor + valor * p
    return result


print(aumento(1000, 0.1))


def divisivel(num):
    if num % 5 == 0 and num % 3 == 0:
        return 'fizzbuzz'
    if num % 5 == 0:
        return 'buzz'
    if num % 3 == 0:
        return 'fizz'

    return num


print(divisivel(7))
print(divisivel(10))
print(divisivel(15))
print(divisivel(22))
