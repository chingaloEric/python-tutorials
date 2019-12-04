#writes a fibonacci up to 'number'
def fibonacci(number):
    a, b= 0, 1
    while(a<number):
        print(a, end=' ')
        a, b = b, a+b
    print(' ')

#fibonacci(7)


#fibonacci function that returns the value
def fibonacci2(number):
    result = []
    a, b = 0,1
    while(a<number):
        result.append(a)
        a, b = b, a+b
    return result

print(fibonacci2(3))