def numero(x, y):
    numbers = []
    while x < y:
        print(f'top i is {x}')
        numbers.append(x)
        
        x += 1
        
        print(f'Numbers on lists: {numbers}')
        print(f'bottom i is {x}')

print('''Lets learn about lists.
Please type two set of numbers. 
first number must be smaller than the next''')
a = int(input('> '))
b = int(input('> '))

numero(a, b)
