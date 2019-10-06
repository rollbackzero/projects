# define the lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# create the loop and print them
for x in the_count:
    print(f'This is count {x}')

for y in fruits:
    print(f'A fruit of type: {y}')

for z in change:
    print(f'I got {z}')

# build a list, start from an empty one

elements = []

for x in range(0, 6):
    print(f'Add {x} on the lists') 
    elements.append(x)  # append each value into the lists

# print them out
for i in elements:
    print(f'Element was: {i}')
