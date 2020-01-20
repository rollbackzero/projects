ten_things = "Apples Oranges Crows Telephone Light Sugar"   # defined lists

print("Wait there are not 10 things in that list. Lets fix that")

stuff = ten_things.split(' ')    # call split function to create a lists out of strings
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]   # defined another lists

while len(stuff) != 10:  # if length of first list is not 10 
    next_one = more_stuff.pop()  # take the topmost item on the second lists
    print("Adding:", next_one)   # display the item 
    stuff.append(next_one)       # append the pop item to the top of first list
    print(f"There are {len(stuff)} items now.")   # display the length of the first lists

print("There we go: ", stuff)   # display the contents of first list

print("Lets do some things with stuff")

print(stuff[1])   # print second item on the list
print(stuff[-1])  # print the item on the list
print(stuff.pop())  # pop and print item on the lists
print(' '.join(stuff)) # combined the items on the lists and display
print('#'.join(stuff[3:5]))  # access cardinal 3 and ordinal 5 of the lists
