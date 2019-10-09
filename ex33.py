i = 0
n = int(input('please type a number: '))

numbers = []

while i < n:
    print(f'top i is {i}')
    numbers.append(i)

    i += 1

    print(f'Numbers on lists: {numbers}')
    print(f'bottom i is {i}')

print('The numbers on the lists: ')

for num in numbers:
    print(num)
