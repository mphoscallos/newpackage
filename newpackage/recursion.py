def sum_array(array)

    total =0
    for i in array:
        total= total + i
        '''Return sum of all items in array'''
    return total

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def factorial(n):
    if n < 2:
        return 1

    else:
        return n * factorial(n - 1)

def reverse(word):
    rev=word[::-1]
    return rev
