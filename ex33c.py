def numero(x, y):
    numbers = []
    for i in range(x, y):
        print(f'top i is {i}')
        numbers.append(i)
        
        print(f'Numbers on lists: {numbers}')
        print(f'bottom i is {i}')

print('''Lets learn about lists.
Please type two set of numbers. 
first number must be smaller than the next''')
a = int(input('> '))
b = int(input('> '))

numero(a, b)
