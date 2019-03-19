def sum_array(array):
    def sum_array(array):

    total =0
    for i in array:
        total= total + i
        '''Return sum of all items in array'''
    return total



def fibonacci(n):
    '''inefficient recursive function as defined, returns Fibonacci number'''
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

    '''Return nth term in fibonacci sequence'''
def factorial(n):
     if n == 1:
        return n
     else:
        return n * factorial(n-1)



    '''Return n!'''
def reverse(word):
    words = word.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)

    return newSentence


    '''Return word in reverse'''
